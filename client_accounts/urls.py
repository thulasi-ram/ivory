from django.conf.urls import url

from client_accounts.views.client import ClientView
from client_accounts.views.clients import ClientsView
from client_accounts.views.contact import ContactView
from client_accounts.views.contacts import ContactsView
from client_accounts.views.landing import ClientAccountLanding
from client_accounts.views.legal_entities import LegalEntitiesView
from client_accounts.views.legal_entity import LegalEntityView

urlpatterns = [
    url(r'^$', ClientAccountLanding.as_view(), name='landing'),
    url(r'^client/(?P<client_id>.*)', ClientView.as_view(), name='client'),
    url(r'^clients/', ClientsView.as_view(), name='clients'),
    url(r'^legal_entity/(?P<legal_entity_id>.*)', LegalEntityView.as_view(), name='legal_entity'),
    url(r'^legal_entities/', LegalEntitiesView.as_view(), name='legal_entities'),
    url(r'^contact/(?P<contact_id>.*)', ContactView.as_view(), name='contact'),
    url(r'^contacts/', ContactsView.as_view(), name='contacts'),
]
