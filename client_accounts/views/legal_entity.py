# Create your views here.

from rest_framework import status
from rest_framework.response import Response

from client_accounts.models import LegalEntity
from client_accounts.schemas import LegalEntitySchema
from common.views import BaseAPI


class LegalEntityView(BaseAPI):

    def get(self, request, *args, **kwargs):
        legal_entity_uid = request.query_params.get('legal_entity_id') or kwargs.get('legal_entity_id')
        legal_entity = LegalEntity.objects.get(uid=legal_entity_uid)
        legal_entity_data, errors = LegalEntitySchema().dump(legal_entity)
        return Response(data=legal_entity_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        legal_entity_schema = LegalEntitySchema().load(request.data)
        LegalEntity.objects.create(**legal_entity_schema)
        return Response(data={'request': request}, status=status.HTTP_201_CREATED)
