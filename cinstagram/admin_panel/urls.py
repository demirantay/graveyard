from django.urls import path, include
from . import views

urlpatterns = [
    # Admin Panel Dashboard
    path("panel/admin/dashboard/", views.admin_panel_dashboard, name="admin_panel_dashboard"),
]
