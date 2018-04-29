# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from common.views import BaseAPI
from lead_management.models import Lead
from lead_management.schemas import LeadSchema


class LeadsView(BaseAPI):

    def get(self, request, *args, **kwargs):
        stage = request.query_params.get('stage')
        leads = Lead.objects.filter(created_by=request.user)
        if stage:
            leads = leads.filter(stage=stage)
        else:
            leads = leads.exclude(stage=Lead.Stage.CLOSED)
        schema = LeadSchema(many=True)
        return Response(data=schema.dump(leads).data, status=status.HTTP_200_OK)
