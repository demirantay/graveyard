from django.urls import path, include
from . import views

urlpatterns = [
    # Explore Page
    path("explore/", views.explore, name="explore"),
]
