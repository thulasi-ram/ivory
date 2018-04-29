# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from client_accounts.models import ClientAccount
from client_accounts.schemas import ClientAccountSchema
from common.views import BaseAPI


class ClientView(BaseAPI):

    def get(self, request, *args, **kwargs):
        client_id = kwargs.get('client_id')
        client_account = ClientAccount.objects.get(uid=client_id)
        client_account_data, errors = ClientAccountSchema().dump(client_account)
        return Response(data=client_account_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        client_account_schema = ClientAccountSchema().load(request.data)
        ClientAccount.objects.create(**client_account_schema)
        return Response(data={'request': request}, status=status.HTTP_201_CREATED)
