from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from api import views
from django.urls import path


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
]