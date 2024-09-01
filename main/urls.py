from django.urls import path
from .views import HomeTestLogin

urlpatterns = [
    
    ###Test
    path('homelog/', HomeTestLogin.as_view(), name='homelog'),

    ##TEST BORRAR
]