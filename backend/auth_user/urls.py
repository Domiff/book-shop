from django.urls import path

from .views import Login, Logout, RegisterUserView

app_name = "auth_user"

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
