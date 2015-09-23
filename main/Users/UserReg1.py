#encoding=utf-8
# Django libraries
from django.http import HttpResponse
from django.core.mail import send_mail
from django.db.models import Q
# Python system libraries
import json,random,sys
# Models
from main.UserModels import User,EmailValidationRecord
# Settings
from CloudWebsite import settings

# Validation email template
EMAIL_TEMPLATE = u"<p>您注册了未来云计算官网的用户，请点击<a href='%s'>此处</a>完成注册。</p>"
EMAIL_TEMPLATE_PLAIN = u"您注册了未来云计算官网的用户，请前往%s完成注册。"
EMAIL_TITLE = u"未来云计算团队 注册确认"

# User registration
def POST(request):
    # Refuse to register if the user already logged
    if ("Logged" in request.session) and (request.session["Logged"]==True):
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"AlreadyLogged"}),content_type="application/json")
    
    # Find if there is a user with same name or email
    _Email = request.POST.get("Email","")
    _Username = request.POST.get("Username","")
    _Password = request.POST.get("Password","")
    SearchResult = User.objects.filter(Q(Email=_Email)|Q(Username=_Username))
    # User found
    if len(SearchResult)!=0:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"DuplicatedUserNameOrEmail"}),content_type="application/json")
    
    # Create email validation record and save record
    EmailRecord = EmailValidationRecord()
    EmailRecord.Email = _Email
    EmailRecord.RedirectAddr = "https://"+request.get_host()+"/Dynamic/Users/UserReg2"
    EmailRecord.Nonce = random.randint(0,sys.maxint)
    EmailRecord.Data = json.dumps({"Email":_Email,"Username":_Username,"Password":_Password})
    # Make email validation address
    ValidationAddr = "https://"+request.get_host()+"/Dynamic/Users/EmailValidation?Nonce=%d&Email=%s" % (EmailRecord.Nonce,_Email)

    try:
        # Render e-mail content
        EmailPlain = EMAIL_TEMPLATE_PLAIN % ValidationAddr
        EmailHTML = EMAIL_TEMPLATE % ValidationAddr
        
        # Send e-mail to address
        send_mail(EMAIL_TITLE, EmailPlain, settings.EMAIL_HOST_USER, [_Email], fail_silently=False, html_message=EmailHTML)
        # Save the record only when the email is successfully sent
        EmailRecord.save()
    # Failed to send mail
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"FailedToSendMail"}),content_type="application/json")
    
    # Successfully send mail, return success
    return HttpResponse(json.dumps({"Status":"Success"}),content_type="application/json")
