from django.contrib.auth import get_user_model
from django.db import models
from djutil.models import TimeStampedModel

from common.middlewares.current_user import get_current_user
from common.models import Address
from common.utils import make_meanigful_id


class LegalEntity(TimeStampedModel):
    uid = models.CharField(max_length=20, editable=False)
    name = models.CharField(max_length=500)
    business_type = models.CharField(max_length=500)
    gstin = models.CharField(max_length=500, default='', blank=True)
    company_email = models.EmailField(max_length=2000, default='', blank=True)
    company_phone = models.CharField(max_length=2000, default='', blank=True)
    created_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, default=get_current_user,
                                   editable=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    notes = models.TextField()

    @property
    def legal_name(self):
        return '{n} {t}'.format(n=self.name, t=self.business_type)

    def __str__(self):
        return self.legal_name

    def __unicode__(self):
        return self.legal_name

    class Meta:
        verbose_name = 'Legal Entity'
        verbose_name_plural = 'Legal Entities'

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = make_meanigful_id(self.name, length=10)
        super().save(*args, **kwargs)


class ClientAccount(TimeStampedModel):
    uid = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    legal_account = models.ForeignKey(LegalEntity, null=True, on_delete=models.SET_NULL)
    handled_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name='handled_by',
                                   default=get_current_user)
    created_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name='created_by',
                                   default=get_current_user, editable=False)
    notes = models.TextField()

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = make_meanigful_id(self.name, length=10)
        super().save(*args, **kwargs)


class ClientAccountAddresses(TimeStampedModel):
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    client_account = models.ForeignKey(ClientAccount, null=True, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=20, blank=True, default='')


class Contact(TimeStampedModel):
    client_account = models.ForeignKey(ClientAccount, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, default=get_current_user)
    designation = models.CharField(max_length=100)
    notes = models.TextField()
