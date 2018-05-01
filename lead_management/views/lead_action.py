# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from common.auth import CsrfExemptSessionAuthentication
from common.views import BaseAPI
from lead_management import lead_action_handlers


class LeadActionView(BaseAPI):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        action_type = request.data.get('action_type')
        lead_id = kwargs.get('lead_id')
        handler = lead_action_handlers.get_handler(action_type)
        handler().handle(lead_id=lead_id, user=request.user, **request.data)
        return Response(data={}, status=status.HTTP_200_OK)
