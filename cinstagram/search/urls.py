from django.urls import path, include
from . import views

urlpatterns = [
    # Search: Account
    path("search/account/", views.search_account, name="search_account"),
    # Search: Hashtag
    path("search/hashtag/", views.search_hashtag, name="search_hashtag"),
    # Search: Location
    path("search/location/", views.search_location, name="search_location"),
]
