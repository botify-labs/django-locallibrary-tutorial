"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework_swagger.views import get_swagger_view

from django.conf.urls import url
from django.contrib import admin

# Use include() to add URLS from the catalog application and authentication system
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


schema_view = get_swagger_view(title='Django Local Library')

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^swagger/$', schema_view),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
