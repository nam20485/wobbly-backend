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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

swagger_view = get_swagger_view(title='Wobbly API')

schema_view = get_schema_view(title='Wobbly API')

urlpatterns = [
    # DRF
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title='Wobbly API')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # swagger
    url(r'^swagger/', swagger_view),
    
    # admin interface
    url(r'^admin/', admin.site.urls),

    # user accounts
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
