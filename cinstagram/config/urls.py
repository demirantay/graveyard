from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    # The admin panel that comes shipped with django
    path("admin/", admin.site.urls),   # remove this and add your ownadminpanel


    # Programmer Panel
    # ----------------
    # This is where the neccessary views regarding the programmer panel app of
    # the site is included, the programmer_panel is a dashboard and a control
    # panel for the programmers(super-users) of the site, yes the "admin" is a
    # superuser too but admin mostly deals with the content of the site, where
    # the programm--ers deal with site-realibity, graphs of the bandwith
    # usaage ... etc.
    path("", include("programmer_panel.urls")),


    # Admin Panel
    # -----------------
    # This is the admin panel where the staff (admins) of the companyoverseethe
    # content that is being entered to the site, polices it, limits it ... etc.
    # The difference between programmer panel is that admins are more oriented
    # towards user entries and not sysadmin control
    path("", include("admin_panel.urls")),


    # Help Centre
    # -----------------
    # This is the app where the staff (admin) of the company updates thecertain
    # information regarding the usage of the site, what are new or howtousethem
    path("", include("help_centre.urls")),


    # About
    # -----------------
    # This app shows the history, who they are, goals of the company ... etcThe
    # most important functionality in this app is the job postings and the jobs
    path("", include("about.urls")),


    # API Website
    # -----------------
    # This app is just the GUI web interface for the usage of the API ofthesite
    # It does not contain any code that creates the API code. It is just a read
    # -only site
    path("", include("api_web.urls")),


    # Authentication
    # ----------------
    # These blueprints contains the user authentication system for the endusers
    # of the site such as the "average joe" and not admin, top tier user ..etc.
    path("", include("authentication.urls")),


    # Profile Settings
    # ----------------
    # This is the app where the user of the site canchangetheiraccoutnsSettings
    # such as changing the password, allowing email and sms messages ... etc.
    path("", include("profile_settings.urls")),


    # Media Upload
    # ----------------
    # This is kinda the core of the application where the users upload pictures
    # or videos. Self note for future: I will need to updatetheimagerecognition
    # so that the site will not be NSFW
    path("", include("media_upload.urls")),


    # Profile
    # ----------------
    # This app contains the landing page of the user, followers, likers, tagged
    # bookmarked photos single post pages ... etc. Everything that is relatedto
    # a user with private, public viewing options ... etc.
    path("", include("profile_app.urls")),


    # Chat
    # ----------------
    # This is the chat application where the users can chat with eachother.Itis
    # pretty self explanatory
    path("", include("chat.urls")),


    # Home
    # ----------------
    # This is the home page which is just actually asinglecontianerthatincludes
    # user specific feeds, alerts, notifications ... etc.
    path("", include("home.urls")),


    # Search Pages
    # ----------------
    # search pages include three search indexes 1 - account searches, 2 hashtag
    # searches and finally 3 - location searches
    path("", include("search.urls")),


    # Explore
    # ----------------
    # Explore page is a simple container just like the home pageitconsistsofnew
    # and unseen and suggested account pictures videos to the current user
    path("", include("explore.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
