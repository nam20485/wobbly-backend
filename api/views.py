from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from api import models, serializers
from api import forms


class SignUp(generic.CreateView):
    """
    Class Form for creating an account
    """
    form_class = forms.WobblyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class WobblyUserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = models.WobblyUser.objects.all()
    serializer_class = serializers.WobblyUserSerializer

class WobblyGroupViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = models.WobblyGroup.objects.all()
    serializer_class = serializers.WobblyGroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class KeywordViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = models.Keyword.objects.all()
    serializer_class = serializers.KeywordSerializer
