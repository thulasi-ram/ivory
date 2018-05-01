from django.conf.urls import url

from lead_management.views.landing import LeadManagementLanding
from lead_management.views.lead import LeadView
from lead_management.views.lead_action import LeadActionView
from lead_management.views.leads import LeadsView

urlpatterns = [
    url(r'^$', LeadManagementLanding.as_view(), name='landing'),
    url(r'^lead/(?P<lead_id>.*)/action/', LeadActionView.as_view(), name='lead-action'),
    url(r'^lead/(?P<lead_id>.*)$', LeadView.as_view(), name='lead'),
    url(r'^leads/', LeadsView.as_view(), name='leads'),
]
