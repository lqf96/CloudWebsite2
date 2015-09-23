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
    NewUserData = json.loads(request.session["EmailValidationData"])
    
    NewUser.Email = NewUserData["Email"]
    NewUser.Username = NewUserData["Username"]
    NewUser.Password = NewUserData["Password"]
    NewUser.save()
    
    # Log user in
    request.session["Logged"] = True
    request.session["Email"] = NewUserData["Email"]
    request.session["Username"] = NewUserData["Username"]
    
    # Redirect to main page
    return HttpResponseRedirect("https://"+request.get_host())
