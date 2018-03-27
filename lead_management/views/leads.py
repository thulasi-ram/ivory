# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from common.views import BaseAPI
from lead_management.models import Lead
from lead_management.schemas import LeadSchema


class LeadsView(BaseAPI):

    def get(self, request, *args, **kwargs):
        leads = Lead.objects.all()
        schema = LeadSchema(many=True, strict=True)
        return Response(data=schema.dump(leads).data, status=status.HTTP_200_OK)
