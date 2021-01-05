# Main Imports

# Django Imports
from django.db import models
from django.utils import timezone

# My Module Imports
from authentication.models import CinstagramUser
from profile_settings.models import CinstagramUserSettings


# Follower/d
# -------------
# This model holds the accounts that fallow an account and also the owner
# account that is being followed
class UserFollowing(models.Model):
    # Followed account info
    followed_id = models.IntegerField(blank=False, null=False)
    followed_user = models.ForeignKey(
        CinstagramUser,
        on_delete=models.CASCADE,
        related_name="followed_user",
        null=True, blank=True
    )
    followed_user_settings = models.ForeignKey(
        CinstagramUserSettings,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="followed_user_settings",
    )

    # Follower account info
    follower_id = models.IntegerField(blank=False, null=False)
    follower_user = models.ForeignKey(
        CinstagramUser,
        on_delete=models.CASCADE,
        related_name="follower_user",
        null=True,
        blank=True
    )
    follower_user_settings = models.ForeignKey(
        CinstagramUserSettings,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="follower_user_settings",
    )

    def __str__(self):
        return "Followed account: (id: %s) %s | Follower account: (id: %s) %s"\
                % (self.followed_id, self.followed_user,
                   self.follower_id, self.follower_user)
