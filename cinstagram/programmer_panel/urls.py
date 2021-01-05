from django.urls import path, include
from . import views

urlpatterns = [
    # Admin Panel Dashboard
    path("panel/programmer/dashboard/", views.programmer_panel_dashboard, name="programmer_panel_dashboard"),
]
