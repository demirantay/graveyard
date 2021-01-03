from django.contrib import admin
from .models import Desk, DeskWorkers, DeskToDo, Article, ArticleComment

admin.site.register(Desk)
admin.site.register(DeskWorkers)
admin.site.register(DeskToDo)
admin.site.register(Article)
admin.site.register(ArticleComment)
