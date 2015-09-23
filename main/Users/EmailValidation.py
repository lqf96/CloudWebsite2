# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
# Python system libraries
import string,json
# Models
from main.UserModels import EmailValidationRecord

# Email validation
def GET(request):
    _Email = request.GET.get("Email","")
    _Nonce = string.atoi(request.GET.get("Nonce",""))
    try:
        ValidationRecord = EmailValidationRecord.objects.get(Email=_Email,Nonce=_Nonce)
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"ValidationInfoNotMatch"}),content_type="application/json")
    
    # Allow access to "internal" address
    request.session["Internal"] = True
    # Store data
    request.session["EmailValidationData"] = ValidationRecord.Data
    # Remove validation record
    ValidationRecord.delete()
    
    # Redirect to given address
    return HttpResponseRedirect(ValidationRecord.RedirectAddr)
