# Main site URL configuration file

# Django libraries
from django.conf.urls import url
# CloudWebsite foundation
from CloudWebsite.CWFoundation import MakeURLList
# Main application packages
import Users, DZ

urls = []
# User API paths
MakeURLList(urls,"Users","Dynamic/")
# Discussion zone API paths
MakeURLList(urls,"DZ","Dynamic/")
