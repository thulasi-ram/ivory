from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.
from djutil.models import TimeStampedModel

from client_accounts.models import ClientAccount


class Lead(TimeStampedModel):
    client_account = models.ForeignKey(ClientAccount, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    stage = models.CharField(max_length=20)
