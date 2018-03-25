from django.contrib.auth import get_user_model
from django.db import models
from djutil.models import TimeStampedModel

from common.models import Address
from common.utils import make_meanigful_id


class LegalEntity(TimeStampedModel):
    uid = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    business_type = models.CharField(max_length=500)
    gstin = models.CharField(max_length=500, default='', blank=True)
    company_email = models.EmailField(max_length=2000, default='', blank=True)
    company_phone = models.CharField(max_length=2000, default='', blank=True)
    created_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    notes = models.TextField()

    def save(self, *args, **kwargs):
        if self.uid is None:
            self.uid = make_meanigful_id(self.name, length=10)
        super().save(*args, **kwargs)


class LegalAccountAddresses(TimeStampedModel):
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    legal_account = models.ForeignKey(LegalEntity, null=True, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=20, blank=True, default='')


class ClientAccount(TimeStampedModel):
    uid = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    legal_account = models.ForeignKey(LegalEntity, null=True, on_delete=models.SET_NULL)
    handled_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name='handled_by')
    created_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name='created_by')
    notes = models.TextField()

    def save(self, *args, **kwargs):
        if self.uid is None:
            self.uid = make_meanigful_id(self.name, length=10)
        super().save(*args, **kwargs)


class ClientAccountAddresses(TimeStampedModel):
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    client_account = models.ForeignKey(ClientAccount, null=True, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=20, blank=True, default='')


class Contact(TimeStampedModel):
    client_account = models.ForeignKey(ClientAccount, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    designation = models.CharField(max_length=100)
    notes = models.TextField()
