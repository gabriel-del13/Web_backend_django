from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, ValidateRegisterView

urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('validatereg/', ValidateRegisterView.as_view(), name='validate-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]