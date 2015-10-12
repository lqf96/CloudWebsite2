# Django libraries
from django.http import HttpResponse,Http404
from django.conf.urls import url
# Python system libraries
import json,re,inspect
from datetime import datetime

# ===== Routing utils =====
# Make URL list (Core function)
def __MakeURLList(url_list,obj,path_list,prefix):
    for child_name in obj.__dict__:
        # Ignore built-in object
        if child_name[:2]=="__":
            continue
        # Push into stack
        path_list.append(child_name)
        # Module
        if "__path__" not in obj.__dict__[child_name].__dict__:
            def __MakeURLListHelper(_path_list,handler_module):
                # Wrapper function
                def Wrapper(request):
                    try:
                        return handler_module.__dict__[request.method](request)
                    # No handler, return 404
                    except KeyError:
                        raise Http404
                url_list.append(url("^"+prefix+"/".join(_path_list)+"$",Wrapper))
            # Call helper (to avoid lambda-related problems)
            __MakeURLListHelper(path_list,obj.__dict__[child_name])
        # Package
        else:
            __MakeURLList(url_list,obj.__dict__[child_name],path_list,prefix)
        # Pop
        path_list.pop()

# Make URL list from API paths (v2)
def MakeURLList(url_list,package_name,prefix=""):
    # Path list
    path_list = [package_name,]
    obj = inspect.currentframe().f_back.f_globals[package_name]
    # Enter core function
    __MakeURLList(url_list,obj,path_list,prefix)

# ===== View utils =====
# "Internal" view
def InternalView(view):
    def NewView(request):
        # Internal access not granted
        if ("Internal" not in request.session) or (request.session["Internal"]==False):
            return HttpResponse(json.dumps({"Status":"Failed","Reason":"InternalAccessNotGranted"}))
        # Access internal view
        result = view(request)
        # Disable internal access unless explicitly stated
        if ("KeepInternal" not in request.session) or (request.session["KeepInternal"]==False):
            request.session["Internal"] = False
        return result
    return NewView

# ===== Data utils =====
# Make time string
def TimeStr(time_obj):
    return time_obj.strftime("%a, %d %b %Y %H:%M:%S GMT")