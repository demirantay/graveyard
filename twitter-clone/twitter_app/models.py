from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

# USER SETTINGS MODEL FOR CHANGING THE PROFILE SETTINGS
class ProfileSettingsModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    profile_photo = CloudinaryField('image')
    first_name = models.CharField(max_length=20, null=True, blank=True)
    bio = models.CharField(max_length=140, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    personal_link = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.first_name

# TWEETS(user entries) MODEL
class TweetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tweets')
    tweet_content = models.CharField(max_length=280)
    publish_date = models.DateField(default=timezone.now)
    tweet_likes = models.IntegerField(default=0)
    tweet_retweets = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username+': ' + self.tweet_content[:30] + '...'


# RETWEETS MODEL
class RetweetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_retweeted')
    retweet = models.ForeignKey(TweetModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='retweet')
    retweet_settings = models.ForeignKey(ProfileSettingsModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='retweet_settings')
    retweet_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username


# FOLLOWING SYSTEM MODEL
class FollowModel(models.Model):
    follower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                blank=True, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                blank=True, related_name='followed' )

    def __str__(self):
        return 'Follower: ' + self.follower.username + ' / Followed: ' + self.followed.username
