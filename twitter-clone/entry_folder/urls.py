from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Twitter app
    path('', include('twitter_app.urls')),

    # Users (auth system)
    path('', include('django.contrib.auth.urls'))
]
