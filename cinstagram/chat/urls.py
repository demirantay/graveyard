from django.urls import path, include
from . import views

urlpatterns = [
    # Chat Index
    path("chat/", views.chat_index, name="chat_index"),
    # New Chat Page
    path("chat/new/", views.new_chat, name="new_chat"),
    # Single Chat Page
    path("chat/<str:username>/", views.single_chat, name="single_chat"),
]
