from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Nombre')
    last_name = forms.CharField(max_length=30, label='Apellido')
    phone_number = forms.CharField(max_length=8, label='Número de teléfono')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user