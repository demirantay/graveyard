from django.urls import path, include
from . import views

urlpatterns = [
    # To-Do tasks page
    path('<str:deskname>/todo/', views.to_do, name='to_do'),
    # New Article create page
    path('<str:deskname>/article/new/', views.new_article, name='new_article'),
    # In Progress page
    path("<str:deskname>/article/progress/", views.in_progress, name='in_progress'),
    # Edit Article page
    path(
        "<str:deskname>/article/edit/<int:article_id>/", views.article_edit,\
        name="article_edit"
    ),
    # Done page
    path("<str:deskname>/done", views.done, name="done"),
]
