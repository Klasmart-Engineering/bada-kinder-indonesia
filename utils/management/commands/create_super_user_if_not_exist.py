from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create Super User if not Exist'

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            username='admin', 
            defaults={
                'password': '', 
                'email': 'it-ops-id@kidsloop.live',
                'is_superuser': True,
                'is_staff': True
            }
        )
        if not created:
            self.stdout.write('superuser already exist, all good')
        else:
            user.set_password(settings.DEFAULT_ADMIN_PASSWORD)
            user.save()
            self.stdout.write('superuser successfully created')
