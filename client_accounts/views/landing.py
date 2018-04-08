# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.response import Response

from common.views import BaseAPI


class ClientAccountLanding(LoginRequiredMixin, BaseAPI):
    template_name = "client_accounts/landing.html"

    def get(self, request, *args, **kwargs):
        return Response(data={'request': request}, template_name=self.template_name, status=status.HTTP_200_OK)
