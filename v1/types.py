from django.contrib.auth import get_user_model

from graphene_django import DjangoObjectType

from core.models import Forum, Post, Thread

User = get_user_model()


class ForumType(DjangoObjectType):
    class Meta:
        model = Forum


class ThreadType(DjangoObjectType):
    class Meta:
        model = Thread


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class UserType(DjangoObjectType):
    class Meta:
        model = User
