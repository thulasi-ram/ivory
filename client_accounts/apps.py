from django.apps import AppConfig


class ClientAccountsConfig(AppConfig):
    name = 'client_accounts'

    def ready(self, **kwargs):
        from actstream import registry
        from client_accounts.models import ClientAccount, LegalEntity
        registry.register(ClientAccount)
        registry.register(LegalEntity)
