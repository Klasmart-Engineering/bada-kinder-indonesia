# Generated by Django 3.2.13 on 2022-07-11 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0006_auto_20220711_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='hide_activity_book',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='hide_course_book',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='hide_story_book',
        ),
    ]
