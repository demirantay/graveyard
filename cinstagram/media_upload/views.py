# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from authentication.models import CinstagramUser
from .models import UserPhoto, UserPhotoComment, UserPhotoLike
from .models import UserPhotoBookmark


def upload_page(request):
    """
    This page lets the user upload an image or vide and than lets it select
    a filter for it. And at the end the form promprts the user to add
    hashtags, captions, locations ... etc.
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    empty_credentials = False

    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_cinstagram_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
    except ObjectDoesNotExist:
        current_cinstagram_user = None

    # Media Upload Validation
    if request.POST.get("media_upload_submit_btn"):
        photo = request.FILES.get("upload_file")
        caption = request.POST.get("caption")
        location = request.POST.get("location")

        # check if the file input is empty
        if bool(photo) is False:
            empty_credentials = True
        else:
            new_photo = UserPhoto(
                user=current_cinstagram_user, photo=photo,
                caption=caption, location=location
            )
            new_photo.save()
            return HttpResponseRedirect("/home/")

    data = {
        "empty_credentials": empty_credentials,
        "current_cinstagram_user": current_cinstagram_user,
    }

    return render(request, "media_upload/upload.html", data)
