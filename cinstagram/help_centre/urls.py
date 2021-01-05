from django.urls import path, include
from . import views

urlpatterns = [
    # Help Centre Index
    path("help_centre/", views.help_centre_index, name="help_centre_index"),
    # Help Centre: Using Instagram
    path("help_centre/using_instagram/", views.help_centre_using_instagram,
         name="help_centre_using_instagram"),
    # ...
]
