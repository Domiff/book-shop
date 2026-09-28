from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField


class CreateUserForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")
        return password_confirm
