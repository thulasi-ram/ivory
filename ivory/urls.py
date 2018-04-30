"""ivory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from common.views import Landing

urlpatterns = [url(r'^$', Landing.as_view(), name='landing'),
               path('admin/', admin.site.urls),
               url(r'^accounts/', include('allauth.urls')),
               url(r'^client_accounts/', include(('client_accounts.urls', 'client_accounts'))),
               url(r'^lead_management/', include(('lead_management.urls', 'lead_management'))),
               url(r'^user_profile/', include(('user_profile.urls', 'user_profile'))),
               url('^activity/', include('actstream.urls')),

               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
