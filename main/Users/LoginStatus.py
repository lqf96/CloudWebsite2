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
