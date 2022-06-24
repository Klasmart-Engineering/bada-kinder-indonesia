from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    package_id = models.IntegerField(default=0, null=True, blank=True)
    user = models.OneToOneField(
        User, 
        null=True, 
        blank=True, 
        related_name='subscription', 
        on_delete=models.SET_NULL
    )


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        null=True, 
        blank=True, 
        related_name='profile', 
        on_delete=models.SET_NULL
    )
    display_name = models.CharField(max_length=128, null=True, blank=True)
    banner = models.FileField( null=True, blank=True, upload_to='media')


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    hide_activity_book = models.BooleanField(default=False)
    hide_course_book = models.BooleanField(default=False)
    hide_story_book = models.BooleanField(default=False)
