from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from . import models


class SubscriptionInline(admin.TabularInline):
    model = models.Subscription


class UserProfileInline(admin.TabularInline):
    model = models.UserProfile


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin,self).__init__(*args, **kwargs)
        UserAdmin.list_display = ['username', 'date_joined']

    def get_form(self, request, obj, **kwargs):
        form = super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['username'].label = 'Email'
        form.base_fields['username'].help_text = ''
        return form

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    
    inlines = [
        UserProfileInline,
        SubscriptionInline,
    ]

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
