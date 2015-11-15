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
    if request.user.is_authenticated():
        return HttpResponse(json.dumps({"Status":"Success", \
            "Logged":True, \
            "Email":request.user.email, \
            "Username":request.user.username}), \
            content_type="application/json")
    # Not logged
    else:
        return HttpResponse(json.dumps({"Status":"Success","Logged":False}),content_type="application/json")

# [Helper Functions]
# Log-in only view decorator
def Login(view):
    def LoginView(request):
        # User logged
        if request.user.is_authenticated():
            return view(request)
        # Not logged
        else:
            return HttpResponse(json.dumps({"Status":"Failed","Reason":"UserNotLogged"}))
    return LoginView

# Log-out only view decorator
def Logout(view):
    def LogoutView(request):
        # User not logged
        if not request.user.is_authenticated():
            return view(request)
        # Not logged
        else:
            return HttpResponse(json.dumps({"Status":"Failed","Reason":"UserAlreadyLogged"}))
    return LogoutView
