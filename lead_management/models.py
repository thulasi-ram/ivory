from django.db import models
from djutil.models import TimeStampedModel

from client_accounts.models import ClientAccount
from common.middlewares.current_user import get_current_user
from common.utils import make_meanigful_id
from user_profile.models import User


class Designation(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class LeadStage(TimeStampedModel):
    uid = models.CharField(max_length=20, unique=True, editable=False)
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = make_meanigful_id('', length=10)
        super().save(*args, **kwargs)


class Lead(TimeStampedModel):
    uid = models.CharField(max_length=20, editable=False, unique=True)
    client_account = models.ForeignKey(ClientAccount, on_delete=models.CASCADE)
    contact = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user, related_name='lead_contact')
    designation = models.ForeignKey(Designation, null=True, on_delete=models.SET_NULL, default=get_current_user)
    stage = models.ForeignKey(LeadStage, null=True, on_delete=models.SET_NULL)

    # created / handled by
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='lead_created_by',
                                   default=get_current_user, editable=False)
    handled_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='lead_handled_by',
                                   default=get_current_user)
    active = models.BooleanField(default=True)
    notes = models.TextField(default='', blank=True)

    has_been_called = models.BooleanField(default=False)
    has_been_sent_profile = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = make_meanigful_id('', length=10)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ("client_account", "contact", "handled_by")
