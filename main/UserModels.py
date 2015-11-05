# Django libraries
from django.db import models

# User groups
class Group(models.Model):
    Name = models.CharField(max_length=64)
    Users = models.ManyToManyField("User")

# Users
class User(models.Model):
    Email = models.EmailField()
    Password = models.CharField(max_length=32)
    Username = models.CharField(max_length=32)

# Email validation records
class EmailValidationRecord(models.Model):
    Email = models.EmailField()
    Nonce = models.BigIntegerField()
    RedirectAddr = models.CharField(max_length=128)
    Data = models.TextField()
