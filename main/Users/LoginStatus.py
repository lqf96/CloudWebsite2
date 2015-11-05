# Django libraries
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
# Python system libraries
import json

# Check log-in status
# (Ensure CSRF token is sent to the client when opening the website)
@ensure_csrf_cookie
def GET(request):
    # Logged
    if ("Logged" in request.session) and (request.session["Logged"]==True):
        return HttpResponse(json.dumps({"Status":"Success",
            "Logged":True,
            "Email":request.session["Email"],
            "Username":request.session["Username"]}))
    # Not logged
    else:
        return HttpResponse(json.dumps({"Status":"Success","Logged":False}))

# [Helper Functions]
# Log-in only view decorator
def Login(view):
    def LoginView(request):
        # User logged
        if ("Logged" in request.session) and (request.session["Logged"]==True):
            return view(request)
        # Not logged
        else:
            return HttpResponse(json.dumps({"Status":"Failed","Reason":"UserNotLogged"}))
    return LoginView

# Log-out only view decorator
def Logout(view):
    def LogoutView(request):
        # User not logged
        if ("Logged" not in request.session) or (request.session["Logged"]==False):
            return view(request)
        # Not logged
        else:
            return HttpResponse(json.dumps({"Status":"Failed","Reason":"UserAlreadyLogged"}))
    return LogoutView
