from django.urls import path, include
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    # Signup
    path('home/signup/', views.signup, name="signup"),
    # Login Gate
    path('home/login/', views.login_gate, name='login_gate'),
    # Dashboard
    path('<str:officename>/home/dashboard/', views.dashboard, name='dashboard'),
    # Desk
    path('<str:officename>/home/desk/', views.desk_browse, name='desk_browse'),
    # Search
    path("home/search/", views.search, name="search"),
    # Publish
    path("home/publish/", views.publish, name="publish"),
]
