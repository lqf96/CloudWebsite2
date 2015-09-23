"""
CloudWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# Django libraries
from django.conf.urls import include, url
from django.contrib import admin
# Django xadmin ibrary
#import xadmin
# CloudWebsite foundation
from CWFoundation import MakeURLList
# Main application packages
from main import Users, DZ

# Auto discover
#xadmin.autodiscover()
admin.autodiscover()
#from xadmin.plugins import xversion
#xversion.register_models()

# Basic URL list
urlpatterns = [
    # Admin URLs
    #url(r'^xadmin/',include(xadmin.site.urls)),
    url(r'^admin/',include(admin.site.urls)),
]

# ===== Main Application =====
# User API paths
urlpatterns += MakeURLList([
    "Users.UserReg1",
    "Users.UserReg2",
    "Users.Login",
    "Users.Logout",
    "Users.LoginStatus",
    "Users.EmailValidation"
],"Dynamic/",Users)

# Discussion zone API paths
urlpatterns += MakeURLList([
    "DZ.GetBoard",
    "DZ.GetBoardList",
    "DZ.GetPost",
    "DZ.NewPost",
    "DZ.NewReply"
],"Dynamic/",DZ)