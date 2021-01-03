from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from profile_app.models import ProfileSettings
from home_app.models import Office


# DESK'S
class Desk(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    sub_editor = models.ForeignKey(User, on_delete=models.CASCADE)
    office = models.ForeignKey(
        Office, on_delete=models.CASCADE, null=True, blank=True
    )
    image = models.ImageField(
        upload_to='deks_images/', blank=False, null=False
    )
    CATEGORY_CHOICES = (
        ('WORLD', 'fa fa-globe'),
        ('METRO', 'fa fa-building'),
        ('POLITICS', 'fa-flag'),
        ('BUSINESS', 'fa fa-suitcase'),
        ('TECH', 'fa fa-code'),
        ('SCIENCE', 'fa fa-flask'),
        ('OPINION', 'fa fa-gavel'),
        ('HEALTH', 'fa fa-heart'),
        ('SPORTS', 'fa fa-bicycle'),
        ('ARTS', 'fa fa-paint-brush'),
        ('BOOKS', 'fa fa-book'),
        ('STYLE', 'fa fa-eye'),
        ('TRAVEL', 'fa fa-plane'),
        ('MAGAZINE', 'fa fa-file'),
        ('TABLOID', 'fa fa-phone'),
    )
    CATEGORY_COLOR_CHOICES = (
        ('WORLD', '#3498DB'),
        ('METRO', '#2980B9'),
        ('POLITICS', '#5D6D7E'),
        ('BUSINESS', '#2E4053'),
        ('TECH', '#F4D03F'),
        ('SCIENCE', '#2ECC71'),
        ('OPINION', '#9B59B6'),
        ('HEALTH', '#E74C3C'),
        ('SPORTS', '#58D68D'),
        ('ARTS', '#F39C12'),
        ('BOOKS', '#E67E22'),
        ('STYLE', '#F5B7B1'),
        ('TRAVEL', '#BB8FCE'),
        ('MAGAZINE', '#8E44AD'),
        ('TABLOID', '#A569BD'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    category_color = models.CharField(
        max_length=50, choices=CATEGORY_COLOR_CHOICES
    )
    name = models.CharField(max_length=30)
    description = models.TextField()
    creation_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


# DESK WORKERS
class DeskWorkers(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_desk = models.ForeignKey(Desk, on_delete=models.CASCADE)

    def __str__(self):
        return self.worker.username


# DESK TO-DO
class DeskToDo(models.Model):
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.desk.name


# DESK ARTICLE
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_settings = models.ForeignKey(
            ProfileSettings, on_delete=models.CASCADE, null=True
        )
    desk = models.ForeignKey('Desk', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50)
    pushed_to_done = models.BooleanField(default=False)
    pushed_to_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.author.username + ' | ' + self.title[:50] + "..."


# ARTICLE COMMENTS
class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.article.title
