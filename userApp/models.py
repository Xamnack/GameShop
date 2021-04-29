from django.conf import settings
from django.db import models

from django.contrib.auth.models import User, UserManager


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='usersPhoto/', blank=True)

    def __str__(self):
        return 'Profile for user {0}'.format(self.user.username)