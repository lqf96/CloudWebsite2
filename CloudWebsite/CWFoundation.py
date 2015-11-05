# Django libraries
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.conf.urls import url
# Python system libraries
import json,inspect
from datetime import datetime
# Site settings
from CloudWebsite.settings import FRONT_END_SERVER

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
                    if request.method in handler_module.__dict__:
                        return handler_module.__dict__[request.method](request)
                    # No handler, return 404
                    else:
                        raise Http404
                # Build django routing object
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
# Internal view decorator
def InternalView(view):
    # Decorated view
    def IView(request):
        # Check if internal access is allowed
        if ("Internal" in request.session) and (request.session["Internal"]==True):
            # Disable internal view access
            request.session["Internal"] = False
            # Append internal arguments to request object
            request.cw_iargs = json.loads(request.session["InternalArgs"])
            del request.session["InternalArgs"]
            # Handle request
            return view(request)
        # Not allowed
        else:
            return HttpResponse(json.dumps({"Status":"Failed","Reason":"InternalAccessNotGranted"}),content_type="application/json")
    return IView

# Redirect to an internal view
def InternalRedirect(address,args):
    # Allow visiting internal view
    request.session["Internal"] = True
    # Save internal arguments to session
    request.session["InternalArgs"] = json.dumps(args) if type(args).__name__=="dict" else argss
    # Do redirection
    return HttpResponseRedirect(address)

# ===== Data utils =====
# Make time string
def TimeStr(time_obj):
    return time_obj.strftime("%a, %d %b %Y %H:%M:%S GMT")

# ===== Cache utils (Not implemented) =====
