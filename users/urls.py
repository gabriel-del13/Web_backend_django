from django.urls import path
from .views import UserRegistrationView, UserLoginView, LoginTest

urlpatterns = [
    
    ###Test
    path('logtest/', LoginTest.as_view(), name='logtest'),
    ##TEST BORRAR
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]