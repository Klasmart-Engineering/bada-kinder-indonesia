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
