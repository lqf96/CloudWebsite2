# Django libraries
from django.http import HttpResponse
# Python system libraries
import json

# Log out
def POST(request):
    # Log user out
    request.session["Logged"] = False
    # Return to index
    return HttpResponse(json.dumps({"Status":"Success"}),content_type="application/json")
