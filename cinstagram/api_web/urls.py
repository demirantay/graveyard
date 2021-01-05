from django.urls import path, include
from . import views

urlpatterns = [
    # API WEB landing page
    path("api_web/", views.api_web, name="api_web"),

    # API WEB register page
    path("api_web/register/", views.api_web_register, name="api_web_register"),

    # API WEB post page
    path("api_web/post/<int:post_id>/", views.api_web_post_page, name="api_web_post_page"),

    # ...

]
