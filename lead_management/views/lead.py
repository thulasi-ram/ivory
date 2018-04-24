# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from common.auth import CsrfExemptSessionAuthentication
from common.views import BaseAPI
from lead_management.models import Lead
from lead_management.schemas import LeadSchema


class LeadView(BaseAPI):
    authentication_classes = (CsrfExemptSessionAuthentication, )

    def get(self, request, *args, **kwargs):
        lead_id = kwargs.get('lead_id')
        lead = Lead.objects.get(uid=lead_id)
        legal_entity_schema = LeadSchema().dump(lead)
        return Response(data=legal_entity_schema, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        lead_schema = LeadSchema().load(request.data)
        Lead.objects.create(**lead_schema)
        return Response(data={'request': request}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        lead_id = kwargs.get('lead_id')
        stage = request.data.get('stage').replace('_', '')
        lead = Lead.objects.get(uid=lead_id)
        lead.stage=stage
        lead.save()
        return Response(data={}, status=status.HTTP_200_OK)
