from dal import autocomplete
from rest_framework import status
from rest_framework.response import Response

from client_accounts.schemas import UserSchema
from common.auth import CsrfExemptSessionAuthentication
from common.views import BaseAPI
from user_profile.models import User


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return User.objects.none()

        qs = User.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class UserProfile(BaseAPI):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    template_name = 'user_profile/user_small.html'

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        if not user_id:
            user_id = request.user.id
        user = User.objects.get(id=user_id)
        user_data, errors = UserSchema().dump(user)
        return Response(data=user_data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = User.objects.get(id=user_id)
        return Response(data={}, status=status.HTTP_200_OK)
