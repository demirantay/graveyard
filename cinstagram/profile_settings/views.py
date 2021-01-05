# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from .models import CinstagramUserSettings
from authentication.models import CinstagramUser


def profile_settings_edit_profile(request):
    """
    In this page the user is able to edit her profile settings such as change
    username, full name, email + add a bio, website url ... etc. and much more
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    empty_credentials = False

    # Get the current user information
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_cinstagram_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
        current_cinstagram_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=current_cinstagram_user
        )
    except ObjectDoesNotExist:
        current_cinstagram_user = None
        current_cinstagram_user_settings = None

    # Edit Profile Form Validation
    if request.POST.get("edit_profile_submit_btn"):
        profile_photo = request.FILES.get("profile_photo")
        full_name = request.POST.get("profile_full_name")
        username = request.POST.get("profile_username")
        personal_url = request.POST.get("profile_url")
        bio = request.POST.get("profile_bio")
        email = request.POST.get("profile_email")
        phone_number = request.POST.get("profile_phone_number")
        gender = request.POST.get("profile_gender")

        if username == "" or email == "":
            # Do not update the model cus there
            # are important empty input fields
            empty_credentials = True
        else:
            # Update the cinstagram user settings model
            current_cinstagram_user_settings.profile_photo = profile_photo
            current_cinstagram_user_settings.full_name = full_name
            current_cinstagram_user_settings.username = username
            current_cinstagram_user_settings.personal_url = personal_url
            current_cinstagram_user_settings.bio = bio
            current_cinstagram_user_settings.email = email
            current_cinstagram_user_settings.phone_number = phone_number
            current_cinstagram_user_settings.gender = gender
            current_cinstagram_user_settings.save()

            # Update the cinstagram user model
            current_cinstagram_user.email = email
            current_cinstagram_user.username = username
            current_cinstagram_user.full_name = full_name
            current_cinstagram_user.save()

    data = {
        "empty_credentials": empty_credentials,
        "current_cinstagram_user": current_cinstagram_user,
        "current_cinstagram_user_settings": current_cinstagram_user_settings,
    }

    return render(request, "profile_settings/edit_profile.html", data)


def profile_settings_change_password(request):
    """
    In this view the casual user is able to change it's password if she enters
    the correct old password and enters a new one
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    invalid_credentials = False

    # Get the current user information
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_cinstagram_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
    except ObjectDoesNotExist:
        current_cinstagram_user = None

    # Change Password Form Validation
    if request.POST.get("change_password_submit_button"):
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        reentered_password = request.POST.get("reentered_password")

        # Check if the user is the owner of the account by
        # asking what is the password is before changing anything
        if old_password == current_cinstagram_user.password:
            # check if entered the correct password on both inputs
            if new_password == reentered_password:
                current_cinstagram_user.password = new_password
                current_cinstagram_user.save()
                return HttpResponseRedirect("/home/")
            else:
                invalid_credentials = True
        else:
            print(old_password)
            print(current_cinstagram_user.password)
            invalid_credentials = True

    data = {
        "invalid_credentials": invalid_credentials,
        "current_cinstagram_user": current_cinstagram_user,
    }

    return render(request, "profile_settings/change_password.html", data)


def profile_settings_email_sms(request):
    """
    In this page the cinstagram users are able to change the settings of the
    email and sms notifications of their accoutns
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    # Get the current user information
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_cinstagram_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
        current_cinstagram_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=current_cinstagram_user
        )
    except ObjectDoesNotExist:
        current_cinstagram_user = None
        current_cinstagram_user_settings = None

    # Sms and Email form validation
    if request.POST.get("sms_email_submit_btn"):
        feedback_emails = request.POST.get("feedback_emails")
        reminder_emails = request.POST.get("reminder_emails")
        product_emails = request.POST.get("product_emails")
        news_emails = request.POST.get("news_emails")
        sms_messages = request.POST.get("sms_messages")

        if feedback_emails == "true":
            current_cinstagram_user_settings.feedback_emails = True
        else:
            current_cinstagram_user_settings.feedback_emails = False

        if reminder_emails == "true":
            current_cinstagram_user_settings.reminder_emails = True
        else:
            current_cinstagram_user_settings.reminder_emails = False

        if product_emails == "true":
            current_cinstagram_user_settings.product_emails = True
        else:
            current_cinstagram_user_settings.product_emails = False

        if news_emails == "true":
            current_cinstagram_user_settings.news_emails = True
        else:
            current_cinstagram_user_settings.news_emails = False

        if sms_messages == "true":
            current_cinstagram_user_settings.sms_messages = True
        else:
            current_cinstagram_user_settings.sms_messages = False

        current_cinstagram_user_settings.save()
        return HttpResponseRedirect("/profile/settings/email_sms/")

    data = {
        "current_cinstagram_user": current_cinstagram_user,
        "current_cinstagram_user_settings": current_cinstagram_user_settings,
    }

    return render(request, "profile_settings/email_sms.html", data)


def profile_settings_privacy_security(request):
    """
    In this view the cinstagram users are able to change the settings of their
    accounts privacy or security such as: turn off the comments ... etc.
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    # Get the current user information
    current_cinstagram_user_email = request.session["cinstagram_user_email"]
    try:
        current_cinstagram_user = CinstagramUser.objects.get(
            email=current_cinstagram_user_email
        )
        current_cinstagram_user_settings = CinstagramUserSettings.objects.get(
            settings_owner=current_cinstagram_user
        )
    except ObjectDoesNotExist:
        current_cinstagram_user = None
        current_cinstagram_user_settings = None

    # Privacy and Security form validation
    if request.POST.get("private_account_submit_btn"):
        private_account = request.POST.get("private_account")
        turn_off_comments = request.POST.get("turn_off_comments")

        if private_account == "true":
            current_cinstagram_user_settings.private_account = True
        else:
            current_cinstagram_user_settings.private_account = False

        if turn_off_comments == "true":
            current_cinstagram_user_settings.turn_off_comments = True
        else:
            current_cinstagram_user_settings.turn_off_comments = False

        current_cinstagram_user_settings.save()
        return HttpResponseRedirect("/profile/settings/privacy_security/")

    data = {
        "current_cinstagram_user": current_cinstagram_user,
        "current_cinstagram_user_settings": current_cinstagram_user_settings,
    }

    return render(request, "profile_settings/privacy_security.html", data)
