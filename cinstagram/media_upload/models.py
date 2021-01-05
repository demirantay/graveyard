# Main Imports

# Django Imports
from django.db import models
from django.utils import timezone

# My Module Imports
from authentication.models import CinstagramUser
from profile_settings.models import CinstagramUserSettings


# User Photos
# -------------
# This model holds the videos that the user uploads to its own profile.
class UserPhoto(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CinstagramUser, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="uploaded_media/", blank=False, null=False
    )
    creation_date = models.DateField(default=timezone.now)
    caption = models.CharField(max_length=2000)
    location = models.CharField(max_length=2000, default="")

    def __str__(self):
        return "Photo id: " + str(self.id) + " | User: " + str(self.user)


# User Photo Comments
# -------------
# This model holds the comments belong to a single UserPhoto post
class UserPhotoComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment_owner = models.ForeignKey(CinstagramUser, on_delete=models.CASCADE)
    comment_owner_settings = models.ForeignKey(
        CinstagramUserSettings,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    commented_photo = models.ForeignKey(UserPhoto, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)
    creation_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Comment Owner: " + str(self.comment_owner) + " | Commented Photo Id: " + str(self.commented_photo.id)


# User Photo Likes
# -----------------
# This model holds the likes that belong toa single UserPhoto post
class UserPhotoLike(models.Model):
    id = models.AutoField(primary_key=True)
    like_owner = models.ForeignKey(CinstagramUser, on_delete=models.CASCADE)
    like_owner_settings = models.ForeignKey(
        CinstagramUserSettings,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    liked_photo = models.ForeignKey(UserPhoto, on_delete=models.CASCADE)

    def __str__(self):
        return "Liked photo id: " + str(self.liked_photo.id) + " | Like Owner: " + str(self.like_owner)


# User Photo Bookmarks
# -----------------
# This model holds the bookmarks that belong toa single UserPhoto post
class UserPhotoBookmark(models.Model):
    id = models.AutoField(primary_key=True)
    bookmark_owner = models.ForeignKey(CinstagramUser, on_delete=models.CASCADE)
    bookmarked_photo = models.ForeignKey(UserPhoto, on_delete=models.CASCADE)
    bookmark_date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return "Bookmarked photo id: " + str(self.bookmarked_photo.id) + " | Bookmark Owner: " + str(self.bookmark_owner)
