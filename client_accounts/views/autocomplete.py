from dal import autocomplete
from django.db.models import Q

from client_accounts.models import ClientAccount, LegalEntity


class ClientAccountAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return ClientAccount.objects.none()

        qs = ClientAccount.objects.filter(handled_by=self.request.user)

        if self.q:
            qs = qs.filter(Q(name__istartswith=self.q) | Q(uid=self.q))

        return qs


class LegalEntityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return LegalEntity.objects.none()

        qs = LegalEntity.objects.filter()

        if self.q:
            qs = qs.filter(Q(name__istartswith=self.q) | Q(uid=self.q))

        return qs


class AddressAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        from common.models import Address

        if not self.request.user.is_authenticated:
            return Address.objects.none()

        qs = Address.objects.all()

        if self.q:
            qs = qs.filter(Q(line1__contains=self.q) | Q(line2__contains=self.q) | Q(city__contains=self.q) |
                           Q(state__contains=self.q) | Q(pincode__contains=self.q) | Q(country__contains=self.q))

        return qs
