#encoding=utf-8
# Django libraries
from django.http import HttpResponse
from django.core.mail import send_mail
# Python system libraries
# Helper functions
from EmailValidation import CreateEmailValidation
from LoginStatus import Logout

# Forget password email template
EMAIL_TEMPLATE = u"<p>请点击<a href='%s'>此处</a>找回您的未来云计算账户密码。</p>"
EMAIL_TEMPLATE_PLAIN = u"您注册了未来云计算官网的用户，请前往%s找回您的未来云计算账户密码。"
EMAIL_TITLE = u"未来云计算团队 密码找回"

# Forget password handler
@Logout
def POST(request):
    # Find user by email
    _Email = request.POST.get("Email","")
    try:
        
