# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from authentication.models import CinstagramUser
from profile_settings.models import CinstagramUserSettings
from media_upload.models import UserPhoto, UserPhotoComment, UserPhotoLike
from media_upload.models import UserPhotoBookmark
from .models import UserFollowing


def profile_single_post_page(request, post_id):
    """
    This view holds all the controller logic for the post system that the usual
    users post. They are generally videos, photos, gifs .. etc.
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

    # Get the current post object
    try:
        post = UserPhoto.objects.get(id=post_id, user=current_user)
    except ObjectDoesNotExist:
        post = None

    # Get the Post Comments
    try:
        post_comments = UserPhotoComment.objects.filter(commented_photo=post)
    except ObjectDoesNotExist:
        post_comments = None

    # Get the Post Likes
    try:
        post_likes = None
    except ObjectDoesNotExist:
        post_likes = None

    # Post Like form Validation
    if request.POST.get("post_like_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Check if the current use has already liked this picture before
        # if she has, then do not like again since a photo can be only
        # liked once by one person
        try:
            filtered_post_liker = UserPhotoLike.objects.get(
                like_owner=current_user
            )
        except ObjectDoesNotExist:
            filtered_post_liker = None

        if filtered_post_liker == None:
            new_like = UserPhotoLike(like_owner=current_user, liked_photo=post)
            new_like.save()
        else:
            pass  # cant like again

    # Post Bookmark From Validaiton
    if request.POST.get("post_bookmark_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Check if the current user already bookmarked this picture
        # if she has do not bookmark it again since it can only be
        # bookmarked once by one person
        try:
            filtered_post_bookmarker = UserPhotoBookmark.objects.get(
                bookmarked_photo=post
            )
        except ObjectDoesNotExist:
            filtered_post_bookmarker = None

        if filtered_post_bookmarker == None:
            new_bookmark = UserPhotoBookmark(
                bookmark_owner=current_user, bookmarked_photo=post
            )
            new_bookmark.save()
        else:
            pass  # cant bookmark again

    # Post Comment form Validation
    if request.POST.get("post_comment_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        comment_content = request.POST.get("comment_content")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Create a new comment for the photo
        new_comment = UserPhotoComment(
            comment_owner=current_user,
            comment_owner_settings=current_user_settings,
            commented_photo=post,
            comment=comment_content
        )
        new_comment.save()

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "post": post,
        "post_comments": post_comments,
    }

    return render(request, "profile/post_page.html", data)


def profile_post_likers(request, post_id):
    """
    This page showcases all of the likers of a given user post such as a photo
    video, gallery ... etc.
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

    # Get the current post object
    try:
        post = UserPhoto.objects.get(id=post_id, user=current_user)
    except ObjectDoesNotExist:
        post = None

    # Get the likers of the project
    try:
        post_likes = UserPhotoLike.objects.filter(liked_photo=post)
    except ObjectDoesNotExist:
        post_likes = None

    # Get the Followers/Followings
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

    # Follow Form processing
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
            return HttpResponseRedirect("/profile/posts/"+str(post_id)+"/likers/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Un-Follow form processing
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
            return HttpResponseRedirect("/profile/posts/"+str(post_id)+"/likers/")

    '''
    SELF NOTE FOR FUTURE AT THE MOMENT I AM NOT IMPLEMENTING THE + BUTTON FORM
    AT THE END OF THE PAGE FOR LOADING MORE DATA, ATM IT JUST LOADS EVERYTHING
    THE TABLE HOLDS. BUT IN THE FUTURE I WILL CHANGE IT SINCE IT IS BAD FOR
    LOADING EVERY ENTRY FROM THE DATA
    '''

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "post": post,
        "post_likes": post_likes,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
    }

    return render(request, "profile/likers.html", data)


def profile_followers(request):
    """
    In this page the user can see all the followers of her account. And she
    can follow or unfollow them.
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

    # Get the Accounts that Follow Current User
    try:
        accounts_following_current_user = UserFollowing.objects.filter(
            followed_user=current_user,
        )
    except ObjectDoesNotExist:
        accounts_following_current_user = None

    # Follow Form processing
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
            return HttpResponseRedirect("/profile/followers/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Un-Follow form processing
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
            return HttpResponseRedirect("/profile/followers/")

    '''
    SELF NOTE FOR FUTURE AT THE MOMENT I AM NOT IMPLEMENTING THE + BUTTON FORM
    AT THE END OF THE PAGE FOR LOADING MORE DATA, ATM IT JUST LOADS EVERYTHING
    THE TABLE HOLDS. BUT IN THE FUTURE I WILL CHANGE IT SINCE IT IS BAD FOR
    LOADING EVERY ENTRY FROM THE DATA
    '''

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
        "accounts_following_current_user": accounts_following_current_user,
    }

    return render(request, "profile/followers.html", data)


def profile_following(request):
    """
    In this page the user can see all the followings of her account. And she
    can follow or unfollow them.
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

    # Follow Form processing
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
            return HttpResponseRedirect("/profile/following/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Un-Follow Form Processing
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
            return HttpResponseRedirect("/profile/following/")

    '''
    SELF NOTE FOR FUTURE AT THE MOMENT I AM NOT IMPLEMENTING THE + BUTTON FORM
    AT THE END OF THE PAGE FOR LOADING MORE DATA, ATM IT JUST LOADS EVERYTHING
    THE TABLE HOLDS. BUT IN THE FUTURE I WILL CHANGE IT SINCE IT IS BAD FOR
    LOADING EVERY ENTRY FROM THE DATA
    '''

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
    }

    return render(request, "profile/following.html", data)


def profile_posts_page(request):
    """
    This is the main landing page of the profile of the user. Whenever they
    click on their profile page or username they get redirected to here and
    from here they get riderected to other pages of the profile such as
    settings, tagged imgs, saved imgs, ... etc.
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

    # Get the Post Count
    try:
        posts = UserPhoto.objects.filter(user=current_user)
        post_count = 0
        for post in posts:
            post_count += 1
    except ObjectDoesNotExist:
        post_count = 0

    # Get the Follower Count
    try:
        followers = UserFollowing.objects.filter(followed_user=current_user)
        follower_count = 0
        for follower in followers:
            follower_count += 1
    except ObjectDoesNotExist:
        follower_count = 0

    # Get the Following Count
    try:
        followings = UserFollowing.objects.filter(follower_user=current_user)
        following_count = 0
        for following in followings:
            following_count += 1
    except ObjectDoesNotExist:
        following_count = 0

    #  Get All of the Users Posts and the posts meta data such as like count, .
    try:
        all_posts = UserPhoto.objects.filter(user=current_user)\
            .order_by('-creation_date')
        # Getting meta info of the posts
        all_posts_likes = {}
        all_posts_comments = {}
        for post in all_posts:
            # Getting the like count
            likes_count = 0
            current_post_likes = UserPhotoLike.objects.filter(liked_photo=post)
            for like in current_post_likes:
                likes_count += 1
            all_posts_likes[post.id] = likes_count
            # Getting the comment count
            comment_count = 0
            current_post_comments = UserPhotoComment.objects\
                .filter(commented_photo=post)
            for comment in current_post_comments:
                comment_count += 1
            all_posts_comments[post.id] = comment_count

    except ObjectDoesNotExist:
        all_posts = None
        all_posts_likes = None
        all_posts_comments = None

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "post_count": post_count,
        "follower_count": follower_count,
        "following_count": following_count,
        "all_posts": all_posts,
        "all_posts_likes": all_posts_likes,
        "all_posts_comments": all_posts_comments,
    }

    return render(request, "profile/posts_page.html", data)


def profile_saved(request):
    """
    In this page the user can see all the images that she bookmarked.
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

    # Get the Post Count
    try:
        posts = UserPhoto.objects.filter(user=current_user)
        post_count = 0
        for post in posts:
            post_count += 1
    except ObjectDoesNotExist:
        post_count = 0

    # Get the Follower Count
    try:
        followers = UserFollowing.objects.filter(followed_user=current_user)
        follower_count = 0
        for follower in followers:
            follower_count += 1
    except ObjectDoesNotExist:
        follower_count = 0

    # Get the Following Count
    try:
        followings = UserFollowing.objects.filter(follower_user=current_user)
        following_count = 0
        for following in followings:
            following_count += 1
    except ObjectDoesNotExist:
        following_count = 0

    #  Get All of the Bookmarked Users Posts and the meta data -like count, etc
    try:
        all_bookmarked_posts = UserPhotoBookmark.objects.\
            filter(bookmark_owner=current_user).order_by('-bookmark_date')
        # Getting meta info of the posts
        all_bookmarked_posts_likes = {}
        all_bookmarked_posts_comments = {}

        for post in all_bookmarked_posts:
            # Getting the like count
            likes_count = 0
            current_bookmarked_post_likes = UserPhotoLike.objects.filter(
                liked_photo=post.bookmarked_photo
            )
            for like in current_bookmarked_post_likes:
                likes_count += 1
            all_bookmarked_posts_likes[post.id] = likes_count

            # Getting the Comment count
            comment_count = 0
            current_post_comments = UserPhotoComment.objects\
                .filter(commented_photo=post.bookmarked_photo)
            for comment in current_post_comments:
                comment_count += 1
            all_bookmarked_posts_comments[post.id] = comment_count

    except ObjectDoesNotExist:
        all_bookmarked_posts = None
        # Getting meta info of the posts
        all_bookmarked_posts_likes = None
        all_bookmarked_posts_comments = None

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "post_count": post_count,
        "follower_count": follower_count,
        "following_count": following_count,
        "all_bookmarked_posts": all_bookmarked_posts,
        "all_bookmarked_posts_likes": all_bookmarked_posts_likes,
        "all_bookmarked_posts_comments": all_bookmarked_posts_comments,
    }

    return render(request, "profile/saved_page.html", data)


def profile_tagged(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    """
        This view will be skipped for now because i do not have the
        tag system up and running
    """

    data = {

    }

    return render(request, "profile/tagged_page.html", data)


# -------------------- OTHER USER PROFILES -----------------------

def other_users_profile_single_post_page(request, username, post_id):
    """
    This view holds all the controller logic for the post system that the usual
    users post. They are generally videos, photos, gifs .. etc.
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

    # Get the Other User
    try:
        other_user = CinstagramUser.objects.get(username=username)
    except ObjectDoesNotExist:
        other_user = None

    # Get the Other User Settings
    try:
        other_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=other_user
        )
    except ObjectDoesNotExist:
        other_user_settings = None

    # Get the current post object
    try:
        post = UserPhoto.objects.get(id=post_id, user=other_user)
    except ObjectDoesNotExist:
        post = None

    # Get the Post Comments
    try:
        post_comments = UserPhotoComment.objects.filter(commented_photo=post)
    except ObjectDoesNotExist:
        post_comments = None

    # Get the Post Like Count
    try:
        post_like_count = None
    except ObjectDoesNotExist:
        post_like_count = None

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

    # Get the Accounts that Follow Current User
    try:
        accounts_following_current_user = UserFollowing.objects.filter(
            followed_user=current_user,
        )
    except ObjectDoesNotExist:
        accounts_following_current_user = None

    if request.POST.get("follow_submit_btn"):
        hidden_user_id = request.POST.get("hidden_user_id")
        hidden_user = CinstagramUser.objects.get(id=hidden_user_id)
        hidden_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=hidden_user
        )
        # Check if the user already has a `follow` relationship with thecurrent
        # user, if there is do nothing. If there is not create new relationship
        # dont forget to add that a user cannot follow itself
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/posts/" + str(post_id) + "/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Other User Un-follow form Validation
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/posts/" + str(post_id) + "/")

    # Post Like form Validation
    if request.POST.get("post_like_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Check if the current use has already liked this picture before
        # if she has, then do not like again since a photo can be only
        # liked once by one person
        try:
            filtered_post_liker = UserPhotoLike.objects.filter(
                like_owner=current_user
            )
        except ObjectDoesNotExist:
            filtered_post_liker = None

        if filtered_post_liker == None:
            new_like = UserPhotoLike(like_owner=current_user, liked_photo=post)
            new_like.save()
        else:
            pass  # cant like again

    # Post Bookmark From Validaiton
    if request.POST.get("post_bookmark_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Check if the current user already bookmarked this picture
        # if she has do not bookmark it again since it can only be
        # bookmarked once by one person
        try:
            filtered_post_bookmarker = UserPhotoBookmark.objects.get(
                bookmarked_photo=post
            )
        except ObjectDoesNotExist:
            filtered_post_bookmarker = None

        if filtered_post_bookmarker == None:
            new_bookmark = UserPhotoBookmark(
                bookmark_owner=current_user, bookmarked_photo=post
            )
            new_bookmark.save()
        else:
            pass  # cant bookmark again

    # Post Comment form Validation
    if request.POST.get("post_comment_form_submit_btn"):
        hidden_post_id = request.POST.get("hidden_post_id")
        comment_content = request.POST.get("comment_content")
        post = UserPhoto.objects.get(id=hidden_post_id)
        # Create a new comment for the photo
        new_comment = UserPhotoComment(
            comment_owner=current_user,
            comment_owner_settings=current_user_settings,
            commented_photo=post,
            comment=comment_content
        )
        new_comment.save()

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "other_user": other_user,
        "other_user_settings": other_user_settings,
        "post": post,
        "post_comments": post_comments,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
        "accounts_following_current_user": accounts_following_current_user,
    }

    return render(request, "profile/other_users_post_page.html", data)


def other_users_profile_post_likers(request, username, post_id):
    """
    This page showcases all of the likers of a given user post such as a photo
    video, gallery ... etc.
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

    # Get the Other User
    try:
        other_user = CinstagramUser.objects.get(username=username)
    except ObjectDoesNotExist:
        other_user = None

    # Get the Other User Settings
    try:
        other_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=other_user
        )
    except ObjectDoesNotExist:
        other_user_settings = None

    # Get the current post object
    try:
        post = UserPhoto.objects.get(id=post_id, user=other_user)
    except ObjectDoesNotExist:
        post = None

    # Get the posts likers
    try:
        post_likes = UserPhotoLike.objects.filter(liked_photo=post)
    except ObjectDoesNotExist:
        post_likes = None

    # Get the Followers/Followings of the Current user
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

    # Follow Form processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/posts/" + str(post_id) + "/likers/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Un-Follow form processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/posts/" + str(post_id) + "/likers/")

    '''
    SELF NOTE FOR FUTURE AT THE MOMENT I AM NOT IMPLEMENTING THE + BUTTON FORM
    AT THE END OF THE PAGE FOR LOADING MORE DATA, ATM IT JUST LOADS EVERYTHING
    THE TABLE HOLDS. BUT IN THE FUTURE I WILL CHANGE IT SINCE IT IS BAD FOR
    LOADING EVERY ENTRY FROM THE DATA
    '''

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "other_user": other_user,
        "other_user_settings": other_user_settings,
        "post": post,
        "post_likes": post_likes,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
    }

    return render(request, "profile/other_users_likers.html", data)


def other_users_profile_followers(request, username):
    """
    In this page the user can see all the followers of other users account.
    And the current suer can follow or unfollow them.
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

    # Get the Other User
    try:
        other_user = CinstagramUser.objects.get(username=username)
    except ObjectDoesNotExist:
        other_user = None

    # Get the Other User Settings
    try:
        other_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=other_user
        )
    except ObjectDoesNotExist:
        other_user_settings = None

    # Get the Acounts Other User is Following
    try:
        other_user_followings = UserFollowing.objects.filter(
            follower_user=other_user,
        )
        accounts_other_user_following = []
        for following in other_user_followings:
            accounts_other_user_following.append(following.followed_user)
    except ObjectDoesNotExist:
        other_user_followings = None
        accounts_other_user_following = []

    # Get the Accounts that Follow Other User
    try:
        accounts_following_other_user = UserFollowing.objects.filter(
            followed_user=other_user,
        )
    except ObjectDoesNotExist:
        accounts_following_other_user = None

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

    # Get the Accounts that Follow Current User
    try:
        accounts_following_current_user = UserFollowing.objects.filter(
            followed_user=current_user,
        )
    except ObjectDoesNotExist:
        accounts_following_current_user = None

    # Follow Form processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/followers/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Un-Follow form processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/followers/")

    '''
    SELF NOTE FOR FUTURE AT THE MOMENT I AM NOT IMPLEMENTING THE + BUTTON FORM
    AT THE END OF THE PAGE FOR LOADING MORE DATA, ATM IT JUST LOADS EVERYTHING
    THE TABLE HOLDS. BUT IN THE FUTURE I WILL CHANGE IT SINCE IT IS BAD FOR
    LOADING EVERY ENTRY FROM THE DATA
    '''

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "other_user": other_user,
        "other_user_settings": other_user_settings,
        "other_user_followings": other_user_followings,
        "accounts_other_user_following": accounts_other_user_following,
        "accounts_following_other_user": accounts_following_other_user,
        "accounts_following_other_user": accounts_following_other_user,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
        "accounts_following_current_user": accounts_following_current_user,
    }

    return render(request, "profile/other_users_followers.html", data)


def other_users_profile_following(request, username):
    """
    In this page the user can see all the followings of other users account.
    And the can follow or unfollow them.
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

    # Get the Other User
    try:
        other_user = CinstagramUser.objects.get(username=username)
    except ObjectDoesNotExist:
        other_user = None

    # Get the Other User Settings
    try:
        other_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=other_user
        )
    except ObjectDoesNotExist:
        other_user_settings = None

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

    # Get the Acounts Other User is Following
    try:
        other_user_followings = UserFollowing.objects.filter(
            follower_user=other_user,
        )
        accounts_other_user_following = []
        for following in other_user_followings:
            accounts_other_user_following.append(following.followed_user)
    except ObjectDoesNotExist:
        other_user_followings = None
        accounts_other_user_following = []

    # Follow Form processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/following/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Unfollow Form processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/following/")

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "other_user": other_user,
        "other_user_settings": other_user_settings,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
        "other_user_followings": other_user_followings,
        "accounts_other_user_following": accounts_other_user_following,
    }

    return render(request, "profile/other_users_following.html", data)


def other_users_profile_posts_page(request, username):
    """
    This is the main landing page of the profile of the user. Whenever they
    click on their profile page or username of the other user get redirected
    to here and from here they get riderected to other pages of the profile
    such as tagged imgs, saved imgs, ... etc.
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

    # Get the Other User
    try:
        other_user = CinstagramUser.objects.get(username=username)
    except ObjectDoesNotExist:
        other_user = None

    # Get the Other User Settings
    try:
        other_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=other_user
        )
    except ObjectDoesNotExist:
        other_user_settings = None

    # Get the Post Count
    try:
        posts = UserPhoto.objects.filter(user=other_user)
        post_count = 0
        for post in posts:
            post_count += 1
    except ObjectDoesNotExist:
        post_count = 0

    # Get the Follower Count
    try:
        followers = UserFollowing.objects.filter(followed_user=other_user)
        follower_count = 0
        for follower in followers:
            follower_count += 1
    except ObjectDoesNotExist:
        follower_count = 0

    # Get the Following Count
    try:
        followings = UserFollowing.objects.filter(follower_user=other_user)
        following_count = 0
        for following in followings:
            following_count += 1
    except ObjectDoesNotExist:
        following_count = 0

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

    # Follow Form processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/posts/")
        else:
            # Do nothing since there is arelationship already
            pass

    # Un-Follow Form Processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/posts/")

    #  Get All of the Users Posts and the posts meta data such as like count,
    try:
        all_posts = UserPhoto.objects.filter(user=other_user)\
            .order_by('-creation_date')
        # Getting meta info of the posts
        all_posts_likes = {}
        all_posts_comments = {}
        for post in all_posts:
            # Getting the like count
            likes_count = 0
            current_post_likes = UserPhotoLike.objects.filter(liked_photo=post)
            for like in current_post_likes:
                likes_count += 1
            all_posts_likes[post.id] = likes_count
            # Getting the comment count
            comment_count = 0
            current_post_comments = UserPhotoComment.objects\
                .filter(commented_photo=post)
            for comment in current_post_comments:
                comment_count += 1
            all_posts_comments[post.id] = comment_count
    except ObjectDoesNotExist:
        all_posts = None
        all_posts_likes = None
        all_posts_comments = None

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "other_user": other_user,
        "other_user_settings": other_user_settings,
        "post_count": post_count,
        "follower_count": follower_count,
        "following_count": following_count,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
        "all_posts": all_posts,
        "all_posts_likes": all_posts_likes,
        "all_posts_comments": all_posts_comments,
    }

    return render(request, "profile/other_users_posts_page.html", data)


def other_users_profile_saved(request, username):
    """
    In this page the user can see all the images that other user bookmarked.
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

    # Get the Other User
    try:
        other_user = CinstagramUser.objects.get(username=username)
    except ObjectDoesNotExist:
        other_user = None

    # Get the Other User Settings
    try:
        other_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=other_user
        )
    except ObjectDoesNotExist:
        other_user_settings = None

    # Get the Post Count
    try:
        posts = UserPhoto.objects.filter(user=other_user)
        post_count = 0
        for post in posts:
            post_count += 1
    except ObjectDoesNotExist:
        post_count = 0

    # Get the Follower Count
    try:
        followers = UserFollowing.objects.filter(followed_user=other_user)
        follower_count = 0
        for follower in followers:
            follower_count += 1
    except ObjectDoesNotExist:
        follower_count = 0

    # Get the Following Count
    try:
        followings = UserFollowing.objects.filter(follower_user=other_user)
        following_count = 0
        for following in followings:
            following_count += 1
    except ObjectDoesNotExist:
        following_count = 0

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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/saved/")
        else:
            # Do nothing since there is arelationship already
            pass

        # Un-Follow Form Processing
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
            return HttpResponseRedirect("/profile/" + str(other_user.username)
                                        + "/saved/")

    #  Get All of the Bookmarked Users Posts and the meta data -like count, etc
    try:
        all_bookmarked_posts = UserPhotoBookmark.objects.\
            filter(bookmark_owner=other_user).order_by('-bookmark_date')
        # Getting meta info of the posts
        all_bookmarked_posts_likes = {}
        all_bookmarked_posts_comments = {}

        for post in all_bookmarked_posts:
            # Getting the like count
            likes_count = 0
            current_bookmarked_post_likes = UserPhotoLike.objects.filter(
                liked_photo=post.bookmarked_photo
            )
            for like in current_bookmarked_post_likes:
                likes_count += 1
            all_bookmarked_posts_likes[post.id] = likes_count

            # Getting the Comment count
            comment_count = 0
            current_post_comments = UserPhotoComment.objects\
                .filter(commented_photo=post.bookmarked_photo)
            for comment in current_post_comments:
                comment_count += 1
            all_bookmarked_posts_comments[post.id] = comment_count

    except ObjectDoesNotExist:
        all_bookmarked_posts = None
        # Getting meta info of the posts
        all_bookmarked_posts_likes = None
        all_bookmarked_posts_comments = None

    data = {
        "current_user": current_user,
        "current_user_settings": current_user_settings,
        "other_user": other_user,
        "other_user_settings": other_user_settings,
        "post_count": post_count,
        "follower_count": follower_count,
        "following_count": following_count,
        "current_user_followings": current_user_followings,
        "accounts_current_user_following": accounts_current_user_following,
        "all_bookmarked_posts": all_bookmarked_posts,
        "all_bookmarked_posts_likes": all_bookmarked_posts_likes,
        "all_bookmarked_posts_comments": all_bookmarked_posts_comments,
    }

    return render(request, "profile/other_users_saved_page.html", data)


def other_users_profile_tagged(request, username):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    """
        This view will be skipped for now because i do not have the
        tag system up and running
    """

    data = {

    }

    return render(request, "profile/other_users_tagged_page.html", data)


# -------------------- Public USER PROFILES ---------------------

# only posts listing and single post page, everything else redirects to log in
