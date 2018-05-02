# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseAPI(APIView):
    template_name = None
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer,]
    authentication_classes = (SessionAuthentication, )
    permission_classes = ()

    def dispatch(self, request, *args, **kwargs):
        if self.template_name:
            self.renderer_classes = [TemplateHTMLRenderer] + self.renderer_classes
        return super().dispatch(request, *args, **kwargs)


class Landing(BaseAPI):
    template_name = "ivory/landing.html"

    def get(self, request, *args, **kwargs):
        return Response(data={'request': request}, template_name=self.template_name, status=status.HTTP_200_OK)

class Calendar(BaseAPI):
    template_name = "ivory/calendar.html"

    def get(self, request, *args, **kwargs):
        return Response(data={'request': request}, template_name=self.template_name, status=status.HTTP_200_OK)
