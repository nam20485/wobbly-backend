"""
Serializers for the models
"""

from rest_framework import serializers

from api import models


class WobblyUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for WobblyUser model
    """
    class Meta:
        model = models.WobblyUser
        fields = '__all__'


class WobblyGroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for WobblyGroup model
    """
    class Meta:
        model = models.WobblyGroup
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Post model
    """
    class Meta:
        model = models.Post
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Comment model
    """
    class Meta:
        model = models.Comment
        fields = '__all__'


class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Keyword model
    """
    class Meta:
        model = models.Keyword
        fields = '__all__'
