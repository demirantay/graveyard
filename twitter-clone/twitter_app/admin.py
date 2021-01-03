from django.contrib import admin
from .models import ProfileSettingsModel, TweetModel, FollowModel, RetweetModel

admin.site.register(ProfileSettingsModel)
admin.site.register(TweetModel)
admin.site.register(FollowModel)
admin.site.register(RetweetModel)
