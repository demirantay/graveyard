# Generated by Django 3.0.1 on 2020-01-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphoto',
            name='location',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
