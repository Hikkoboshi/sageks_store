from django import forms

from .models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'phone', 'email')


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password',)