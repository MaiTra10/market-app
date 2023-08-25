from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LogInForm

app_name = "core"

urlpatterns = [
    path("", views.index, name = "index"),
    path("contact/", views.contact, name = "contact"),
    path("signup/", views.signup, name = "signup"),
    path("login/", auth_views.LoginView.as_view(authentication_form = LogInForm, template_name = "core/login.html"), name = "login")
]
