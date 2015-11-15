# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login
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
    login(request,NewUser)
    # Redirect to main page
    return HttpResponseRedirect("https://"+request.get_host())
