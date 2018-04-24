from django.db import models
# Create your models here.
from djutil.models import TimeStampedModel

from client_accounts.models import Contact
from common.middlewares.current_user import get_current_user
from common.utils import make_meanigful_id
from user_profile.models import User


class Lead(TimeStampedModel):
    class Stage:
        IDENTIFY = 'identify'
        PROSPECT = 'prospect'
        SUPPORTER = 'supporter'
        ENQUIRY = 'enquiry'
        BUSINESS = 'business'
        CLOSED = 'closed'

        CHOICES = ((x, x) for x in [IDENTIFY, PROSPECT, SUPPORTER, ENQUIRY, BUSINESS, CLOSED])

    uid = models.CharField(max_length=20, editable=False, unique=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    stage = models.CharField(max_length=20, choices=Stage.CHOICES)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
                                   related_name='lead_created_by',
                                   default=get_current_user, editable=False)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = make_meanigful_id('', length=10)
        super().save(*args, **kwargs)
