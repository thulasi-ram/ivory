from django.contrib.auth import get_user_model
from django.db import models

from djutil.models import TimeStampedModel

User = get_user_model()


def get_full_name(self):
    return self.get_full_name()


User.add_to_class("__str__", get_full_name)


class Salutation(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(null=True, blank=True)
    linkedin_url = models.URLField(default='', blank=True)
    facebook_url = models.URLField(default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    alternate_phone = models.CharField(max_length=15, default='', blank=True)
    alternate_email = models.EmailField(max_length=200, default='', blank=True)
    gender = models.CharField(max_length=15, default='', blank=True)
    salutation = models.ForeignKey(Salutation, null=True, on_delete=models.SET_NULL, blank=True)
