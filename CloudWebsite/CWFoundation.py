# Django libraries
from django.http import HttpResponse,Http404
from django.conf.urls import url
# Python system libraries
import json,re
from datetime import datetime

# ===== Routing utils =====
# Make URL list from API paths
def MakeURLList(path_list,prefix,root_package=None):
    url_list = []
    
    for _path in path_list:
        def MakeURLListHelper(path):
            split_path_list = path.split(".")
            url_handler = None
            
            for i in xrange(len(split_path_list)):
                if i==0:
                    url_handler = root_package if root_package!=None else __import__(split_path_list[0])
                else:
                    url_handler = url_handler.__dict__[split_path_list[i]]
            
            def WrapperFunc(request):
                try:
                    return url_handler.__dict__[request.method](request)
                except KeyError:
                    raise Http404
            
            url_list.append(url("^"+prefix+"/".join(split_path_list)+"$",WrapperFunc))
        
        MakeURLListHelper(_path)
    
    return url_list

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