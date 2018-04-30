from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'user_profile'

    def ready(self, **kwargs):
        from actstream import registry
        from user_profile.models import User
        registry.register(User)
