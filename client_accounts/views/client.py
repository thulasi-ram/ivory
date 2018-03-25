# Create your views here.
from rest_framework import status
from rest_framework.response import Response

from common.views import BaseAPI


class Client(BaseAPI):

    def get(self, request, *args, **kwargs):
        return Response(data={'request': request}, status=status.HTTP_200_OK)
