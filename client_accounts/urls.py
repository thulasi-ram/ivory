from django.conf.urls import url

from client_accounts.views.client import Client
from client_accounts.views.clients import Clients
from client_accounts.views.contact import Contact
from client_accounts.views.contacts import Contacts
from client_accounts.views.landing import ClientAccountLanding
from client_accounts.views.legal_entities import LegalEntities
from client_accounts.views.legal_entity import LegalEntity

urlpatterns = [
    url(r'^$', ClientAccountLanding.as_view(), name='landing'),
    url(r'^client/', Client.as_view(), name='client'),
    url(r'^clients/', Clients.as_view(), name='clients'),
    url(r'^legal_entity/', LegalEntity.as_view(), name='legal_entity'),
    url(r'^legal_entities/', LegalEntities.as_view(), name='legal_entities'),
    url(r'^contact/', Contact.as_view(), name='contact'),
    url(r'^contacts/', Contacts.as_view(), name='contacts'),
]
