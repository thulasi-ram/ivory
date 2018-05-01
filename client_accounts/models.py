from django.db import models
from django.utils.functional import cached_property
from djutil.models import TimeStampedModel

from common.middlewares.current_user import get_current_user
from common.models import Address
from common.utils import make_meanigful_id
from user_profile.models import User


class LegalEntity(TimeStampedModel):
    uid = models.CharField(max_length=20, editable=False)
    name = models.CharField(max_length=500)
    business_type = models.CharField(max_length=500)
    gstin = models.CharField(max_length=500, default='', blank=True)
    company_email = models.EmailField(max_length=2000, default='', blank=True)
    company_phone = models.CharField(max_length=2000, default='', blank=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=get_current_user,
                                   editable=False)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    notes = models.TextField()

    @cached_property
    def legal_name(self):
        return '{n} {t}'.format(n=self.name, t=self.business_type)

    def __str__(self):
        return '{n} ({i})'.format(n=self.legal_name, i=self.uid)

    class Meta:
        verbose_name = 'Legal Entity'
        verbose_name_plural = 'Legal Entities'

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = make_meanigful_id(self.name, length=10)
        super().save(*args, **kwargs)


class ClientAccount(TimeStampedModel):
    uid = models.CharField(max_length=20, editable=False)
    name = models.CharField(max_length=500)
    legal_account = models.ForeignKey(LegalEntity, null=True, on_delete=models.SET_NULL)
    handled_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='account_handled_by',
                                   default=get_current_user)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='account_created_by',
                                   default=get_current_user, editable=False)
    notes = models.TextField()

    def __str__(self):
        return '{n} ({i}) ({u})'.format(n=self.name, u=self.handled_by, i=self.uid)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = make_meanigful_id(self.name, length=10)
        super().save(*args, **kwargs)


class ClientAccountAddresses(TimeStampedModel):
    class AddressType:
        CONTACT = 'contact'
        BILLING = 'billing'
        SHIPPING = 'shipping'

        CHOICES = ((x, x) for x in [CONTACT, BILLING, SHIPPING])

    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    client_account = models.ForeignKey(ClientAccount, null=True, on_delete=models.CASCADE, related_name='addresses')
    address_type = models.CharField(max_length=20, blank=True, default='', choices=AddressType.CHOICES)
