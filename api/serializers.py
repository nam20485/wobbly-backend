from api.models import WobblyUser
from rest_framework import serializers


class WobblyUserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = WobblyUser
        fields = ('id', 'username')