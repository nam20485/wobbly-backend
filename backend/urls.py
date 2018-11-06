"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.views.generic.base import TemplateView
from django.urls import path


swagger_view = get_swagger_view(title='Wobbly API')
schema_view = get_schema_view(title='Wobbly API')

urlpatterns = [
    # DRF
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Wobbly API')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # swagger
    path('swagger/', swagger_view),
    
    # admin interface
    path('admin/', admin.site.urls),

    # api app urls
    path('api/', include('api.urls')),

    # home index
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
