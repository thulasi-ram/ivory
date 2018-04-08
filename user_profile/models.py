from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from djutil.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    birth_day = models.DateField(default='', blank=True)
    linkedin_url = models.URLField(default='', blank=True)
    facebook_url = models.URLField(default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)


User = get_user_model()
