# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# My Module Imports


def about(request):
    # Deleting any sessions regarding top-tier type of users

    data = {

    }

    return render(request, "about/about_index.html", data)


def jobs(request):
    # Deleting any sessions regarding top-tier type of users

    data = {

    }
    return render(request, "about/job_postings.html", data)


def job_post(request, job_id):
    # Deleting any sessions regarding top-tier type of users

    data = {

    }
    return render(request, "about/jobs_post_page.html", data)


def legal(request):
    # Deleting any sessions regarding top-tier type of users

    data = {

    }
    return render(request, "about/legal.html", data)
