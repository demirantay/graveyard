# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My App Imports
from authentication.models import CinstagramUser
from profile_settings.models import CinstagramUserSettings
from media_upload.models import UserPhoto, UserPhotoComment, UserPhotoLike
from media_upload.models import UserPhotoBookmark
from profile_app.models import UserFollowing


def home(request):
    """
    This is the home page of the application. Once a user loggs in this landing
    page greets her. There is a section for notifcation alerts, suggestion box
    es and a feed of following accounts posts on the left side with their
    comments likes ... etc.
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    # Get the current user
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
    except ObjectDoesNotExist:
        current_user = None

    # Get the current user settings
    try:
        current_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=current_user
        )
    except ObjectDoesNotExist:
        current_user_settings = None

    # Get Suggested Accounts
    try:
        # The newest 3 accounts that follow you
        current_user_followers = UserFollowing.objects.filter(
            followed_user=current_user
        )
        suggested_accounts = []
        for follower in current_user_followers:
            suggested_accounts.append(follower)
        # Only get the last three since there is only 3 user cells in the
        # template that they go into
        suggested_accounts = suggested_accounts[-4:-1]
    except ObjectDoesNotExist:
        suggested_accounts = None

    # Get the Acounts Current User is Following
    try:
        current_user_followings = UserFollowing.objects.filter(
            follower_user=current_user,
        )
        accounts_current_user_following = []
        for following in current_user_followings:
            accounts_current_user_following.append(following.followed_user)
    except ObjectDoesNotExist:
        current_user_followings = None
        accounts_current_user_following = []

    # Following form Validation for suggested accounts
    if request.POST.get("follow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        hidden_user = CinstagramUser.objects.get(id=hidden_user_id)
        hidden_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=hidden_user
        )
        # Check if the user already has a `follow` relationship with thecurrent
        # user, if there is do nothing. If there is not create new relationship
        try:
            filtered_follower = UserFollowing.objects.get(
                followed_id=hidden_user.id,
                follower_id=current_user.id,
            )
        except ObjectDoesNotExist:
            filtered_follower = None

        if filtered_follower == None:
            # new relationship
            new_following_relationship = UserFollowing(
                followed_id=hidden_user.id,
                followed_user=hidden_user,
                followed_user_settings=hidden_user_settings,
                follower_id=current_user.id,
                follower_user=current_user,
                follower_user_settings=current_user_settings,
            )
            new_following_relationship.save()
            return HttpResponseRedirect("/home/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Unfollowing form Validation for suggested accounts
    if request.POST.get("unfollow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        hidden_user = CinstagramUser.objects.get(id=hidden_user_id)
        hidden_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=hidden_user
        )
        # Check if the user already has a `follow` relationship with thecurrent
        # user, if there is not do nothing. If there is  delete  relationship
        try:
            filtered_follower = UserFollowing.objects.get(
                followed_id=hidden_user.id,
                follower_id=current_user.id,
            )
        except ObjectDoesNotExist:
            filtered_follower = None

        if filtered_follower == None:
            # do nothing since it does not exists
            pass
        else:
            # delete the relationship
            filtered_follower.delete()
            return HttpResponseRedirect("/home/")


    # Get All of the posts of the users that are followed by the current user

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "suggested_accounts": suggested_accounts,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
    }

    return render(request, "home/home.html", data)
