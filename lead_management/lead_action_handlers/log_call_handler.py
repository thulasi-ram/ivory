from actstream import action
from django.db import transaction

from lead_management.lead_action_handlers.base_handler import BaseActionHandler
from lead_management.models import Lead


class LogCallActionHandler(BaseActionHandler):

    def handle(self, lead_id, user, **kwargs):
        lead = Lead.objects.get(uid=lead_id)
        with transaction.atomic():
            if not lead.has_been_called:
                lead.has_been_called = True
                lead.save()
            action.send(user, verb='called', action_object=lead)
