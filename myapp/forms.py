from django import forms
from .models import Course,Cart
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Course_form(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

class Registrationform(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','username','password']
    
    def save(self):
        old=super().save(commit=False)
        old.password=make_password(self.cleaned_data['password'])
        old.save()
        return old

class Loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput())