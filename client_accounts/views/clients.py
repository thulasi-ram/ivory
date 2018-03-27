# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from client_accounts.models import ClientAccount
from client_accounts.schemas import ClientAccountSchema
from common.views import BaseAPI


class ClientsView(BaseAPI):

    def get(self, request, *args, **kwargs):
        client_accounts = ClientAccount.objects.all()
        schema = ClientAccountSchema(many=True, strict=True)
        return Response(data=schema.dump(client_accounts).data, status=status.HTTP_200_OK)
