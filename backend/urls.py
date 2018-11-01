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
from django.conf.urls import url, include, re_path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from apiv1 import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

swagger_view = get_swagger_view(title='Wobbly API')
schema_view = get_schema_view(title='Wobbly API')

urlpatterns = [
    # DRF
    url(r'^api/v1', include(router.urls)),
    url(r'^api/v1/schema/$', schema_view),
    url(r'^api/v1/docs/', include_docs_urls(title='Wobbly API')),

    # Custom paths that don't neatly fit DRF's automatic routing
    # We don't want a list view of all users
    re_path(r'^api/v1/users/<int:pk>', views.UserDetail.as_view()),

    # Swagger
    url(r'^api/v1/swagger/', swagger_view),

    # Admin interface
    url(r'^admin/', admin.site.urls),
]
