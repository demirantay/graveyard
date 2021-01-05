from django.contrib import admin
from .models import UserPhoto, UserPhotoLike, UserPhotoComment
from .models import UserPhotoBookmark

# Register your models here.
admin.site.register(UserPhoto)
admin.site.register(UserPhotoLike)
admin.site.register(UserPhotoComment)
admin.site.register(UserPhotoBookmark)
