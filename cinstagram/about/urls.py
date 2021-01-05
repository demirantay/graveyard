from django.urls import path, include
from . import views

urlpatterns = [
    # About Landing Page
    path("about/", views.about, name="about"),

    # About Job Post Listings
    path("about/jobs/", views.jobs, name="jobs"),

    # Specific job post
    path("about/jobs/<int:job_id>/", views.job_post, name="job_post"),

    # Legal terms
    path("about/legal/", views.legal, name="legal"),
]
