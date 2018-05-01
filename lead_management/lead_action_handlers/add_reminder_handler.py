from actstream import action

from lead_management.lead_action_handlers.base_handler import BaseActionHandler
from lead_management.models import Lead


class AddReminderActionHandler(BaseActionHandler):

    def handle(self, lead_id, user, **kwargs):
        lead = Lead.objects.get(uid=lead_id)
        action.send(user, verb='added a reminder', target=lead)
