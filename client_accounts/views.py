# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from common.views import BaseAPI


class ClientAccount(BaseAPI):
    template_name = "client_accounts/list.html"

    def get(self, request, *args, **kwargs):
        return Response(data={'request': request}, template_name=self.template_name, status=status.HTTP_200_OK)


class ClientAccountsList(BaseAPI):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "url": "http://127.0.0.1:3434/user/2/",
                "username": "morgoth",
                "first_name": "morgoth",
                "email": "duke.valafar@gmail.com",
                "is_staff": True
            }, {
                "url": "http://127.0.0.1:3434/user/3/",
                "username": "anna",
                "first_name": "",
                "email": "anna@anna.com",
                "is_staff": True
            }, {
                "url": "http://127.0.0.1:3434/user/4/",
                "username": "adam",
                "first_name": "",
                "email": "ada@abc.com",
                "is_staff": False
            }
        ]
        return Response(data=data, status=status.HTTP_200_OK)
