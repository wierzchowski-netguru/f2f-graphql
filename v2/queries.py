import graphene
from graphene_django.filter import DjangoFilterConnectionField

from v2.nodes import ForumNode, PostNode, ThreadNode, UserNode


class Query(graphene.ObjectType):
    forums = DjangoFilterConnectionField(ForumNode)
    threads = DjangoFilterConnectionField(ThreadNode)
    posts = DjangoFilterConnectionField(PostNode)
    users = DjangoFilterConnectionField(UserNode)
