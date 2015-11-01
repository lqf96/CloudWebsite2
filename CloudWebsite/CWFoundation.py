# Django libraries
from django.http import HttpResponse,Http404
from django.conf.urls import url
# Python system libraries
import json,inspect
from datetime import datetime
from copy import copy
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
                url_obj = url("^"+prefix+"/".join(_path_list)+"$",Wrapper)
                url_obj.cw_path = copy(_path_list)
                url_list.append(url_obj)
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

# Get view by path
def GetView(url_list,view_path):
    split_view_path = view_path.split(".")
    # Search for the view path in the list
    for view_url in url_list:
        if ("cw_path" in view_url) and (cmp(view_url.cw_path,split_view_path)==0):
            return view_url.callback
    # View not found
    return None

# ===== View utils =====
# Internal view decorator
def InternalView(view):
    # Decorated view
    def IView(request):
        # Check if internal access is allowed
        if ("Internal" in request.session) and (request.session["Internal"]==True):
            response = view(request)
            # Disable internal view access
            request.session["Internal"] = False
            return response
        # Not allowed
        else:
            return HttpResponse(json.dumps({"Status":"Failed","Reason":"InternalAccessNotGranted"}),content_type="application/json")
    return IView

# Redirect to an internal view
def InternalRedirect(request,next_view,params):
    # Allow visiting internal view
    request.session["Internal"] = True
    # Set internal view parameters
    if "cw_iparams" in request.__dict__:
        del request.cw_iparams
    request.cw_iparams = params
    # Call internal view
    return next_view(request)

# ===== Data utils =====
# Make time string
def TimeStr(time_obj):
    return time_obj.strftime("%a, %d %b %Y %H:%M:%S GMT")

# ===== Cache utils (Not implemented) =====
