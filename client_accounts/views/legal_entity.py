# Create your views here.
from marshmallow import Schema, fields
from rest_framework import status
from rest_framework.response import Response

from common.views import BaseAPI


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()


class LegalEntitySchema(Schema):
    name = fields.Str()
    business_type = fields.Str()
    gstin = fields.Str()
    company_email = fields.Email()
    company_phone = fields.Str()
    notes = fields.Str()
    created_by = fields.Nested(UserSchema)


class LegalEntityView(BaseAPI):

    def get(self, request, *args, **kwargs):
        legal_entity = request.data.get('legal_entity')
        LegalEntity.objects.get()
        return Response(data={'request': request}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response(data={'request': request}, status=status.HTTP_201_CREATED)
