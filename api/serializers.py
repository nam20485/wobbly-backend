from api import models
from rest_framework import serializers


class WobblyUserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.WobblyUser
        fields = ('id', 'username')


class WobblyGroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.WobblyGroup
        #fields = ('id', 'username')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.Post
        #fields = ('id', 'username')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.Comment
        #fields = ('id', 'username')


class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = models.Keyword
        #fields = ('id', 'username')