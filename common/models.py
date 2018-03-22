from django.db import models

# Create your models here.
from django.forms import model_to_dict
from djutil.models import TimeStampedModel


class Address(TimeStampedModel):
    line1 = models.CharField(max_length=255, blank=True, default='')
    line2 = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=200, blank=True, default='')
    state = models.CharField(max_length=200, blank=True, default='')
    pincode = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return '{line1}, {line2}, {city}, {state} - {pincode}, {country}'.format(**self.to_dict())

    def to_dict(self):
        data = model_to_dict(self)
        data.pop('id')
        return data

    def to_string(self):
        return self.__str__()

    def is_empty(self):
        return " ".join(self.to_dict().values()).isspace()
