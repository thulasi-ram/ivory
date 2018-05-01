from django.apps import AppConfig


class LeadManagementConfig(AppConfig):
    name = 'lead_management'

    def ready(self, **kwargs):
        from actstream import registry
        from lead_management.models import Lead
        registry.register(Lead)
