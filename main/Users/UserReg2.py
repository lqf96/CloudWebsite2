# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
# Models
from main.UserModels import User
# Python system libraries
import json
# Project foundation library
from CloudWebsite.CWFoundation import InternalView

# User registration
@InternalView
def GET(request):
    NewUser = User()
    NewUser.Email = request.cw_iargs["Email"]
    NewUser.Username = request.cw_iargs["Username"]
    NewUser.Password = request.cw_iargs["Password"]
    NewUser.save()
    
    # Log user in
    request.session["Logged"] = True
    request.session["Email"] = request.cw_iargs["Email"]
    request.session["Username"] = request.cw_iargs["Username"]
    
    # Redirect to main page
    return HttpResponseRedirect("https://"+request.get_host())
