# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports
from .models import CinstagramUser
from profile_settings.models import CinstagramUserSettings


def authentication_signup(request):
    """
    auth_signup: is the page that seperates the curious noisy anon users
    from the real users. You cannot see other than public profiles if you
    are not signed up and logged into the the app.
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop
    if "cinstagram_user_email" in request.session:
        del request.session["cinstagram_user_email"]
        del request.session["cinstagram_user_username"]
        del request.session["cinstagram_user_logged_in"]

    invalid_credentials = False
    empty_credentials = False

    # Signup Form Validation
    if request.POST.get("signup_submit_btn"):
        email = request.POST.get("email")
        full_name = request.POST.get("fullName")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check if the inputs are empty or not
        if (
            bool(email) is False
            or bool(email.strip()) is False
            or bool(full_name) is False
            or bool(full_name.strip()) is False
            or bool(username) is False
            or bool(username.strip()) is False
            or bool(password) is False
            or bool(password.strip()) is False
        ):
            empty_credentials = True
        else:
            # If it is not empty check if the username exists, if it does
            # do not create a new user
            try:
                user = CinstagramUser.objects.get(username=username)
            except ObjectDoesNotExist:
                user = None

            if user is None:
                # User does not exist so create a new one
                new_user = CinstagramUser(
                    email=email, full_name=full_name,
                    username=username, password=password
                )
                new_user.save()
                # Get the new user and add new settings to that user
                # Reassign the `new_user` variable to get the object not
                # re-inisiate another class instance
                new_user = CinstagramUser.objects.get(
                    email=email, username=username
                )
                new_user_settings = CinstagramUserSettings(
                    settings_owner=new_user, username=username,
                    email=email, full_name=full_name
                )
                new_user_settings.save()
                return HttpResponseRedirect("/auth/login/")
            else:
                # User exists
                invalid_credentials = True

    data = {
        "invalid_credentials": invalid_credentials,
        "empty_credentials": empty_credentials,
    }

    return render(request, "authentication/signup.html", data)


def authentication_login(request):
    """
    There is no need to explain a lot about it this the login for users
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)
    # session.pop("programmer_logged_in", None)
    # admin user session pop
    # admin user session pop
    if "cinstagram_user_email" in request.session:
        del request.session["cinstagram_user_email"]
        del request.session["cinstagram_user_username"]
        del request.session["cinstagram_user_logged_in"]

    invalid_credentials = False
    empty_credentials = False

    # Login Form Validation
    if request.POST.get("login_submit_btn"):
        email = request.POST.get("email")
        password = request.POST.get("password")

        # check if the inputs are empty or not
        if (
            bool(email) is False
            or bool(email.strip()) is False
            or bool(password) is False
            or bool(password.strip()) is False
        ):
            empty_credentials = True
        else:
            # Check if the user credits are right and if they
            # are log the user into the system and add sessions
            try:
                user = CinstagramUser.objects.get(email=email,
                                                  password=password)
            except ObjectDoesNotExist:
                user = None

            if user is None:
                # User does not exist
                invalid_credentials = True
            else:
                # Add the session variables than redirect the user
                request.session["cinstagram_user_email"] = user.email
                request.session["cinstagram_user_username"] = user.username
                request.session["cinstagram_user_logged_in"] = True
                return HttpResponseRedirect("/home/")

    data = {
        "invalid_credentials": invalid_credentials,
        "empty_credentials": empty_credentials,
    }

    return render(request, "authentication/login.html", data)


# Thank you for signig up will be added

# Setting up acount will be added

# Forgot password link will be added
