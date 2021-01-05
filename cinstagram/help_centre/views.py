# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports


def help_centre_index(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "help_centre/main_page.html", data)


def help_centre_using_instagram(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }
    return render(request, "help_centre/topic_page.html", data)


# OTHER HELP CENTRE topic pages VIEWS WILL BE ADDED
# HELP CENTRE POST VIEW WILL BE ADDED
