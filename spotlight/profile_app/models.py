from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# USER SETTINGS
class ProfileSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        upload_to='profile_photos/', blank=True, null=True
    )
    bio = models.TextField(blank=False, null=False)
    personal_link = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.user.username
