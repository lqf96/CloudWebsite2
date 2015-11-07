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
def GET(request,iargs):
    NewUser = User()
    NewUser.Email = iargs["Email"]
    NewUser.Username = iargs["Username"]
    NewUser.Password = iargs["Password"]
    NewUser.save()
    
    # Log user in
    request.session["Logged"] = True
    request.session["Email"] = iargs["Email"]
    request.session["Username"] = iargs["Username"]
    request.session["ID"] = NewUser.id
    
    # Redirect to main page
    return HttpResponseRedirect("https://"+request.get_host())
