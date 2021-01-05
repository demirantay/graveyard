from django.urls import path, include
from . import views

urlpatterns = [
    # Profile Settings Edit Profile
    path("profile/settings/edit_profile/", views.profile_settings_edit_profile, name="profile_settings_edit_profile"),
    # Profile Settings Change Password
    path("profile/settings/change_password/", views.profile_settings_change_password, name="profile_settings_change_password"),
    # Profile Settings Email-sms
    path("profile/settings/email_sms/", views.profile_settings_email_sms, name="profile_settings_email_sms"),
    # Profile Settings privacy security
    path("profile/settings/privacy_security/", views.profile_settings_privacy_security, name="profile_settings_privacy_security"),

]
