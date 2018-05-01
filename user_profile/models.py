from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from djutil.models import TimeStampedModel

User = get_user_model()


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_day = models.DateField(default='', blank=True)
    linkedin_url = models.URLField(default='', blank=True)
    facebook_url = models.URLField(default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    alternate_phone = models.CharField(max_length=15, default='', blank=True)
    alternate_email = models.EmailField(max_length=200, default='', blank=True)
    gender = models.CharField(max_length=15, default='', blank=True)


class Salutation(TimeStampedModel):
    title = models.CharField(max_length=100)
