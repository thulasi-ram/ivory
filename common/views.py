# Create your views here.
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseAPI(APIView):
    template_name = None
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer,)
    authentication_classes = ()
    permission_classes = ()

    def dispatch(self, request, *args, **kwargs):
        if self.template_name:
            self.renderer_classes = (TemplateHTMLRenderer,)
        return super().dispatch(request, *args, **kwargs)


class Landing(BaseAPI):
    template_name = "landing.html"

    def get(self, request, *args, **kwargs):
        return Response(data={'request': request}, template_name=self.template_name, status=status.HTTP_200_OK)
