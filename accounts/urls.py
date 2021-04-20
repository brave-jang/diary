from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.Login, name="login"),
    path("signup/", views.Signup, name="signup"),
    path("logout/", views.logout_view, name="logout")
    ]
