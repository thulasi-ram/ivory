from django.conf.urls import url

from client_accounts.views import ClientAccount, ClientAccountsList

urlpatterns = [
    url(r'^$', ClientAccount.as_view(), name='client_account'),
    url(r'list/', ClientAccountsList.as_view(), name='client_accounts_list'),
]
