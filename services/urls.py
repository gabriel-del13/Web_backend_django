from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    
    #TEST
    path("test/" ,views.test, name="test"),
    
    
    ]

