from django.urls import path, include
from . import views


urlpatterns = [
    # Index Page(log in gate)
    path('', views.index, name='index'),

    # Thanks Page
    path('thanks/', views.thanks, name='thanks'),

    # Profile Page
    path('profile/', views.profile, name='profile'),

    # Following and Followers Page
    path('follow_info/', views.follow_info, name='follow_info'),

    # Settings Page
    path('profile_settings/', views.profile_settings, name='profile_settings'),

    # Other User Page
    path('other_user/<str:username>/', views.other_user_profile, name='other_user_profile'),

    # Other User Follow info page
    path('other_user/<str:username>/follow_info/', views.other_user_follow_info, name='other_user_follow_info'),

    # Home page for recent tweets
    path('home/', views.home, name='home'),

    # Explore page
    path('explore/', views.explore, name='explore')
]
