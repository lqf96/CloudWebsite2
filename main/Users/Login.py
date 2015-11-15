# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login
# Python system libraries
import json
# Models
from main.UserModels import User
# Helper functions
from LoginStatus import Logout

# Log in
@Logout
def POST(request):
    _Email = request.POST.get("Email","")
    _Password = request.POST.get("Password","")
    
    try:
        # Check if user with given email exists
        _User = User.objects.get(email=_Email)
        # Check if password is correct
        LoginFailed = _User.Password!=_Password
    # User not found
    except:
        LoginFailed = True
        
    # Login failed
    if LoginFailed:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"CredentialNotCorrect"}),content_type="application/json")
    
    # Log user in
    login(_User)
    # Return to index
    return HttpResponse(json.dumps({"Status":"Success"}),content_type="application/json")
