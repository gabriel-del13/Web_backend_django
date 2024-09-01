from django.urls import path
from .views import UserRegistrationView, UserLoginView, LoginTest, RegisterTest

urlpatterns = [
    
    ###Test
    path('logtest/', LoginTest.as_view(), name='logtest'),
    path('regtest/', RegisterTest.as_view(), name='regtest'),
    ##TEST BORRAR
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]