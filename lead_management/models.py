from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.
from djutil.models import TimeStampedModel

from client_accounts.models import ClientAccount
from common.middlewares.current_user import get_current_user


class Lead(TimeStampedModel):
    uid = models.CharField(max_length=20, editable=False)
    client_account = models.ForeignKey(ClientAccount, null=True, on_delete=models.SET_NULL)
    contact = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name='lead_contact')
    stage = models.CharField(max_length=20)
    created_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name='lead_created_by',
                                   default=get_current_user, editable=False)
