# Create your views here.
from actstream import action
from rest_framework import status
from rest_framework.response import Response

from common.auth import CsrfExemptSessionAuthentication
from common.views import BaseAPI
from lead_management.models import Lead


class LeadActionView(BaseAPI):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        action_type = request.data.get('action_type')
        lead_id = kwargs.get('lead_id')
        lead = Lead.objects.get(uid=lead_id)
        if action_type == 'log_a_call':
            action.send(request.user, verb='called', action_object=lead)
        elif action_type == 'send_profile':
            action.send(request.user, verb='sent profile', target=lead)
        elif action_type == 'add_a_reminder':
            action.send(request.user, verb='added a reminder', target=lead)
        return Response(data={}, status=status.HTTP_200_OK)
