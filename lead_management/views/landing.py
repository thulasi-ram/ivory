# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.response import Response

from common.views import BaseAPI
from lead_management.models import LeadStage
from lead_management.schemas import LeadStageSchema


class LeadManagementLanding(LoginRequiredMixin, BaseAPI):
    template_name = "lead_management/landing.html"

    def get(self, request, *args, **kwargs):
        lead_stages = LeadStage.objects.all()
        lead_stages_data, errors = LeadStageSchema(many=True).dump(lead_stages)
        return Response(data={'request': request, 'lead_stages': lead_stages_data},
                        template_name=self.template_name, status=status.HTTP_200_OK)
