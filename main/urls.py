from django.urls import path
from .views import HomeTest, HomeTestLogin

urlpatterns = [
    
    ###Test
    path('hometest/', HomeTest.as_view(), name='hometest'),
    path('homelog/', HomeTestLogin.as_view(), name='homelog'),

    ##TEST BORRAR
]