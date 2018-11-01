from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class User(AbstractUser):
    """
    https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#substituting-a-custom-user-model
    """
    nodes = models.ManyToManyField(to='Node', through='Membership')


class Membership(models.Model):
    MEMBERSHIP_TYPES = (
        ('MEM', 'Member'),
        ('MOD', 'Moderator'),
    )
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    node = models.ForeignKey('Node', on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=MEMBERSHIP_TYPES)


class Node(models.Model):
    """
    A group of users. This can be a local node (e.g. a union branch) or a higher-level node with subgroups.
    In higher-level nodes, users are elected delegates from the nodes' children.

    Anything that isn't explicitly set with `blank=True` is required.

    TODO: implement subgroups
    TODO: should all users of descendant nodes have read-only access to higher-level nodes?
    TODO: add metadata to node relationships (i.e. a timestamp for when a child node joined a parent node)
    """
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True)
    # TODO: should nodes be able to join several supernodes?
    # pros: a node like "McDonald's Princes Street" might want to be a part of both the supernodes "McDonald's
    # Edinburgh" and "Fast food workers Edinburgh".
    # cons: this can lead to confusing situations where e.g. "McDonald's Princes Street" is a part of both
    # "McDonald's Edinburgh" and "McDonald's Scotland".
    # The general question here is: how do we either enforce or nudge users towards a sensible node hierarchy?
    # If a parent node is deleted, child nodes remain
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='children')


class Message(models.Model):
    """
    A chat message sent by a user to a node.
    When a user is deleted, all their messages remain but with a dummy "deleted user" account.
    TODO: decide on whether we want a Slack-like or forum-like setup of threads/topics (or something entirely different)
    TODO: for each user, implement the last message they have seen in each node they're in
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.SET(get_sentinel_user()))
    group = models.ForeignKey(Node, on_delete=models.CASCADE)
    content = models.TextField()
    # TODO: editing a message (perhaps only within 10 minutes or so)
    timestamp = models.DateTimeField(auto_now_add=True)
