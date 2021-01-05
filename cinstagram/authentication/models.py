from django.db import models
from django.utils import timezone


# User Model
# ----------------
# This model is the basic user (average joe) of the site. It will be constantly
# imporved in each fucntionality added to the site that the suer can use
class CinstagramUser(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    creation_date = models.DateField(default=timezone.now)

    """
    These foreign keys will be deleted just keeping it for reference abs

    photos = db.relationship("UserPhoto")
    comments = db.relationship("UserPhotoComment")
    likes = db.relationship("UserPhotoLike")
    bookmarks = db.relationship("UserPhotoBookmark")

    """

    def __str__(self):
        return "id: " + str(self.id) + " | username: " + str(self.username)
