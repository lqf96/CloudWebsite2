# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
# Python system libraries
import json
# Models
from main.UserModels import User

# Log in
def POST(request):
    # Triggers error if an logged user wanted to log in again
    if ("Logged" in request.session) and (request.session["Logged"]==True):
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"AlreadyLogged"}),content_type="application/json")
    
    _Email = request.POST.get("Email","")
    _Password = request.POST.get("Password","")
    try:
        _User = User.objects.get(Email=_Email,Password=_Password)
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"CredentialNotCorrect"}),content_type="application/json")
    
    # Log user in
    request.session["Email"] = _Email
    request.session["Username"] = _User.Username
    request.session["Logged"] = True
    
    # Return to index
    return HttpResponse(json.dumps({"Status":"Success"}))
