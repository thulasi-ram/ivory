from django.conf.urls import url

from lead_management.views.landing import LeadManagementLanding

urlpatterns = [
    url(r'^$', LeadManagementLanding.as_view(), name='landing'),
]
