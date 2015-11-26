# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
# Python system libraries
import string,json,random,sys
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
    
    # Redirect internally to given address
    response = InternalRedirect(request,ValidationRecord.RedirectAddr,ValidationRecord.Data)
    # Remove validation record
    ValidationRecord.delete()
    return response

# [Helper Functions]
# Create email validation record
def CreateEmailValidation(email,redirect_addr,data):
    EmailRecord = EmailValidationRecord()
    EmailRecord.Email = email
    EmailRecord.RedirectAddr = redirect_addr
    EmailRecord.Data = json.dumps(data)
    EmailRecord.Nonce = random.randint(0,sys.maxint)
    EmailRecord.save()
    return EmailRecord