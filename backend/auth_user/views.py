from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from auth_user.forms import CreateUserForm


class RegisterUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = "auth_user/registration_app.html"
    success_url = reverse_lazy("auth_user:login")


class Login(LoginView):
    template_name = "auth_user/login_app.html"
    success_url = reverse_lazy("books:main")


class Logout(LogoutView):
    http_method_names = ["get", "post"]
    template_name = "auth_user/logout_app.html"
    next_page = reverse_lazy("books:main")
