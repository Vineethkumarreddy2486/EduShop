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
        model = User
        fields = ['email', 'username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")

        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")

        return email

    def save(self):
        old = super().save(commit=False)
        old.password = make_password(self.cleaned_data['password'])
        old.save()
        return old

class Loginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput())