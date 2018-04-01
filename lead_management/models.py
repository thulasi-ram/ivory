from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.
from djutil.models import TimeStampedModel

from client_accounts.models import Contact
from common.middlewares.current_user import get_current_user
from common.utils import make_meanigful_id


class Lead(TimeStampedModel):
    uid = models.CharField(max_length=20, editable=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    stage = models.CharField(max_length=20)
    created_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL,
                                   related_name='lead_created_by',
                                   default=get_current_user, editable=False)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = make_meanigful_id('', length=10)
        super().save(*args, **kwargs)
