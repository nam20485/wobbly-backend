"""
URL configuration for app-specific URLs
"""
from django.conf.urls import include
from django.urls import path
from graphene_django.views import GraphQLView
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.WobblyUserViewSet)
router.register(r'groups', views.WobblyGroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'keywords', views.KeywordViewSet)
router.register(r'permission', views.PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

]
