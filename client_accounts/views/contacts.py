# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from client_accounts.models import Contact
from client_accounts.schemas import ContactSchema
from common.views import BaseAPI


class ContactsView(BaseAPI):

    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.filter(client_account__handled_by=request.user)
        schema = ContactSchema(many=True, strict=True)
        return Response(data=schema.dump(contacts).data, status=status.HTTP_200_OK)
