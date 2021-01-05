from django.urls import path, include
from . import views

urlpatterns = [
    # Chat Index
    path("upload/", views.upload_page, name="upload_page"),
]
