from django.conf.urls import url

from user_profile.views import UserAutocomplete, UserProfile

urlpatterns = [
    url(r'^$', UserProfile.as_view(), name='user-profile'),
    url(r'^user/(?P<user_id>.*)', UserProfile.as_view(), name='user-detail'),
    url(r'^user-autocomplete', UserAutocomplete.as_view(), name='user-autocomplete'),
]
