from django.contrib import admin
from . import models


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['package_id', 'user']