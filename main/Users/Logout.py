# Django libraries
from django.http import HttpResponse
from django.contrib.auth import logout
# Python system libraries
import json

# Log out
def POST(request):
    # Log user out
    logout(request)
    # Return to index
    return HttpResponse(json.dumps({"Status":"Success"}),content_type="application/json")
