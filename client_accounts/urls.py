from django.conf.urls import url

from client_accounts.views.autocomplete import ClientAccountAutocomplete, LegalEntityAutocomplete, \
    AddressAutocomplete
from client_accounts.views.client import ClientView
from client_accounts.views.clients import ClientsView
from client_accounts.views.landing import ClientAccountLanding
from client_accounts.views.legal_entities import LegalEntitiesView
from client_accounts.views.legal_entity import LegalEntityView

urlpatterns = [
    url(r'^$', ClientAccountLanding.as_view(), name='landing'),
    url(r'^client/(?P<client_id>.*)', ClientView.as_view(), name='client'),
    url(r'^clients/', ClientsView.as_view(), name='clients'),
    url(r'^legal_entity/(?P<legal_entity_id>.*)', LegalEntityView.as_view(), name='legal_entity'),
    url(r'^legal_entities/', LegalEntitiesView.as_view(), name='legal_entities'),

    # autocompletes
    url(r'^client-account-autocomplete', ClientAccountAutocomplete.as_view(), name='client-account-autocomplete'),
    url(r'^legal-entity-autocomplete', LegalEntityAutocomplete.as_view(), name='legal-entity-autocomplete'),
    url(r'^address-autocomplete', AddressAutocomplete.as_view(), name='address-autocomplete'),
]
