from django.contrib.auth import get_user_model

from graphene import relay
from graphene_django import DjangoObjectType

from core.models import Forum, Post, Thread

User = get_user_model()


class ForumNode(DjangoObjectType):
    class Meta:
        model = Forum
        filter_fields = ['id', 'name']
        interfaces = relay.Node,


class ThreadNode(DjangoObjectType):
    class Meta:
        model = Thread
        filter_fields = ['id', 'name']
        interfaces = relay.Node,


class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = ['id', 'text']
        interfaces = relay.Node,


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['id', 'username']
        interfaces = relay.Node,
