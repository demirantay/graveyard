# Generated by Django 2.0.4 on 2018-05-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_auto_20180521_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='type',
            field=models.CharField(choices=[('JOURNALISM', 'Journalism')], max_length=250),
        ),
    ]