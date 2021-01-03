from django.urls import path, include
from . import views

urlpatterns = [
    # Contributions
    path('contributions/', views.contributions, name='contributions'),
    # Desk Management
    path('management/', views.desk_management, name='desk_management'),
    # Settings
    path('<str:officename>/profile/settings/', views.settings, name='settings'),
]
