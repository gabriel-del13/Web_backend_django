from django.shortcuts import render


##Test##
from django.views.generic import TemplateView

class HomeTest(TemplateView):
    template_name = "home.html"
    
class HomeTestLogin(TemplateView):
    template_name = "homelog.html"
    
###

# Create your views here.
