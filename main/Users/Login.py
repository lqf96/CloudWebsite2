# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
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
        _User = User.objects.get(Email=_Email,Password=_Password)
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"CredentialNotCorrect"}),content_type="application/json")
    
    # Log user in
    request.session["Email"] = _Email
    request.session["Username"] = _User.Username
    request.session["ID"] = _User.id
    request.session["Logged"] = True
    
    # Return to index
    return HttpResponse(json.dumps({"Status":"Success"}),content_type="application/json")
