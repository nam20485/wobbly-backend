from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from api import views
from django.urls import path
from api.views import SignUp, WobblyUserViewSet
from graphene_django.views import GraphQLView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', WobblyUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

]