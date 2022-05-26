from django.db import models
from django.utils.translation import gettext_lazy as _


class UsersappModel(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(_('email address'), unique=True, blank=True)


    def __str__(self):
        return self.username


