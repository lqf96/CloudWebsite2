# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
# Python system libraries
import string,json
# Models
from main.UserModels import EmailValidationRecord
# Site foundation library
from CloudWebsite.CWFoundation import InternalRedirect

# Email validation
def GET(request):
    _Email = request.GET.get("Email","")
    _Nonce = string.atoi(request.GET.get("Nonce",""))
    try:
        ValidationRecord = EmailValidationRecord.objects.get(Email=_Email,Nonce=_Nonce)
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"ValidationInfoNotMatch"}),content_type="application/json")
    
    # Store data
    request.session["EmailValidationData"] = ValidationRecord.Data
    # Remove validation record
    ValidationRecord.delete()
    # Redirect internally to given address
    return InternalRedirect("/Internal/")
