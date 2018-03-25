# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from client_accounts.models import LegalEntity
from client_accounts.schemas import LegalEntitySchema
from common.views import BaseAPI


class LegalEntitiesView(BaseAPI):

    def get(self, request, *args, **kwargs):
        legal_entities = LegalEntity.objects.all()
        schema = LegalEntitySchema(many=True, strict=True)
        return Response(data=schema.dump(legal_entities).data, status=status.HTTP_200_OK)
