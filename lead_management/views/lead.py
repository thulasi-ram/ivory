# Create your views here.
from actstream.models import target_stream
from rest_framework import status
from rest_framework.response import Response

from common.auth import CsrfExemptSessionAuthentication
from common.views import BaseAPI
from lead_management.models import Lead, LeadStage
from lead_management.schemas import LeadSchema


def get_json_feed(feed):
    from django.utils.translation import ugettext as _

    ctx = {
        'actor': feed.actor,
        'verb': feed.verb,
        'action_object': feed.action_object,
        'target': feed.target,
    }

    if feed.target:
        if feed.action_object:
            _description = _('%(actor)s %(verb)s %(action_object)s on %(target)s')
        else:
            _description = _('%(actor)s %(verb)s %(target)s')
    elif feed.action_object:
        _description = _('%(actor)s %(verb)s %(action_object)s')
    else:
        _description = _('%(actor)s %(verb)s')
    return {'title': _description % ctx, 'timesince': feed.timesince()}


class LeadView(BaseAPI):
    template_name = 'lead_management/lead.html'
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get(self, request, *args, **kwargs):
        lead_id = kwargs.get('lead_id')
        lead = Lead.objects.get(uid=lead_id)
        lead_data, errors = LeadSchema().dump(lead)
        feed = [get_json_feed(item) for item in target_stream(lead)]
        return Response(data={'lead': lead_data, 'feed': feed}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        lead_schema = LeadSchema().load(request.data)
        Lead.objects.create(**lead_schema)
        return Response(data={'request': request}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        lead_id = kwargs.get('lead_id')
        stage_id = request.data.get('stage')
        lead = Lead.objects.get(uid=lead_id)
        stage = LeadStage.objects.get(uid=stage_id)
        lead.stage = stage
        lead.save()
        return Response(data={}, status=status.HTTP_200_OK)
