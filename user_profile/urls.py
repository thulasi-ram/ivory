from django.conf.urls import url

from user_profile.views import UserAutocomplete

urlpatterns = [
    url(r'^user-autocomplete', UserAutocomplete.as_view(), name='user-autocomplete'),
]
