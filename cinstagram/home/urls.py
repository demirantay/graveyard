from django.urls import path, include
from . import views

urlpatterns = [
    # Chat Index
    path("home/", views.home, name="home"),
]
