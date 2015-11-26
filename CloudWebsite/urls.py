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
# Main application URL configuration
from main.urls import urls as main_urls

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

# Main site URLs
urlpatterns += main_urls
