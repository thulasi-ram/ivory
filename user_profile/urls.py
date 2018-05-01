from django.conf.urls import url

from user_profile.views import UserAutocomplete, UserProfile

urlpatterns = [
    url(r'^user/(?P<username>.*)', UserProfile.as_view(), name='user-profile'),
    url(r'^user-autocomplete', UserAutocomplete.as_view(), name='user-autocomplete'),
]
