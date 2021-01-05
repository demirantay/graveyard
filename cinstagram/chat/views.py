# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports


def chat_index(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "chat/index_page.html", data)


def new_chat(request):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }
    return render(request, "chat/new_chat.html", data)


def single_chat(request, username):
    """ ... """
    # Deleting any sessions regarding top-tier type of users

    data = {

    }
    return render(request, "chat/single_chat.html", data)
