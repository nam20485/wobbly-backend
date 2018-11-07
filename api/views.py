from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from api.forms import WobblyUserCreationForm
from api.serializers import WobblyUserSerializer
from api.models import WobblyUser


class SignUp(generic.CreateView):
    form_class = WobblyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class WobblyUserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = WobblyUser.objects.all()
    serializer_class = WobblyUserSerializer
