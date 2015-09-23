# Django libraries
from django.db import models

# User table
class User(models.Model):
    Email = models.EmailField()
    Password = models.CharField(max_length=32)
    Username = models.CharField(max_length=32)
    
    class Meta:
        app_label = "main"

# Email validation records
class EmailValidationRecord(models.Model):
    Email = models.EmailField()
    Nonce = models.BigIntegerField()
    RedirectAddr = models.CharField(max_length=192)
    Data = models.TextField()
    
    class Meta:
        app_label = "main"