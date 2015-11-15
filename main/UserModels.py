# Django libraries
from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Users (Inherited from Django user)
# (Properties with same name are used to ensure compatibility)
class User(DjangoUser):
    # Email property
    @property
    def Email(self):
        return self.email
    @Email.setter
    def Email(self,_email):
        self.email = _email
    
    # Password helper class
    class __PasswordHelper():
        # Init with current user reference
        def __init__(self,user):
            self.__user = user
        # Check if stored password matches given password
        def __eq__(self,pswd):
            return self.__user.check_password(pswd)
    # Password property
    @property
    def Password(self):
        return User.__PasswordHelper(self)
    @Password.setter
    def Password(self,pswd):
        self.set_password(pswd)
    
    # Username property
    @property
    def Username(self):
        return self.username
    @Username.setter
    def Username(self,name):
        self.username = name

# Email validation records
class EmailValidationRecord(models.Model):
    Email = models.EmailField()
    Nonce = models.BigIntegerField()
    RedirectAddr = models.CharField(max_length=128)
    Data = models.TextField()
