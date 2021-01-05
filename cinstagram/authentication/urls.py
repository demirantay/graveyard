from django.urls import path, include
from . import views

urlpatterns = [
    # Signup
    path("auth/signup/", views.authentication_signup, name="authentication_signup"),

    # Login
    path("auth/login/", views.authentication_login, name="authentication_login"),

]
