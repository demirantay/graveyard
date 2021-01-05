from django.urls import path, include
from . import views

urlpatterns = [
    # Proifle Single Posts Page
    path("profile/posts/<int:post_id>/", views.profile_single_post_page, name="profile_single_post_page"),
    # Profile Likers
    path("profile/posts/<int:post_id>/likers/", views.profile_post_likers, name="profile_post_likers"),
    # Profile Followers
    path("profile/followers/", views.profile_followers, name="profile_followers"),
    # Profile Following
    path("profile/following/", views.profile_following, name="profile_following"),
    # Profile Posts Page
    path("profile/posts/", views.profile_posts_page, name="profile_posts_page"),
    # Profile Saved
    path("profile/saved/", views.profile_saved, name="profile_saved"),
    # Profile Tagged
    path("profile/tagged/", views.profile_tagged, name="profile_tagged"),
    # Other Users Proifle Single Posts Page
    path(
        "profile/<str:username>/posts/<int:post_id>/",
        views.other_users_profile_single_post_page,
        name="other_users_profile_single_post_page"
    ),
    # Other Users Profile Likers
    path(
        "profile/<str:username>/posts/<int:post_id>/likers/",
        views.other_users_profile_post_likers,
        name="other_users_profile_post_likers"
    ),
    # Other Users Profile Followers
    path(
        "profile/<str:username>/followers/",
        views.other_users_profile_followers,
        name="other_users_profile_followers"
    ),
    # Other Users Profile Following
    path(
        "profile/<str:username>/following/",
        views.other_users_profile_following,
        name="other_users_profile_following"
    ),
    # Other Users Profile Posts Page
    path(
        "profile/<str:username>/posts/",
        views.other_users_profile_posts_page,
        name="other_users_profile_posts_page"
    ),
    # Other Users Profile Saved
    path(
        "profile/<str:username>/saved/",
        views.other_users_profile_saved,
        name="other_users_profile_saved"
    ),
    # Other Users Profile Tagged
    path(
        "profile/<str:username>/tagged/",
        views.other_users_profile_tagged,
        name="other_users_profile_tagged"
    ),
]
