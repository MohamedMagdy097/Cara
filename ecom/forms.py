from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Massage
            
class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['address','mobile','profile_pic']
        

class MassageForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = ['email', 'subject', 'msg']
        
