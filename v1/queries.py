import graphene

from core.models import Forum, Post, Thread
from v1.types import ForumType, PostType, ThreadType, User, UserType


class Query(graphene.ObjectType):
    forums = graphene.List(ForumType)
    threads = graphene.List(ThreadType)
    posts = graphene.List(PostType)
    users = graphene.List(UserType)

    me = graphene.Field(UserType)

    def resolve_forums(self, info, **kwargs):
        return Forum.objects.all()

    def resolve_threads(self, info, **kwargs):
        return Thread.objects.all()

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Please provide valid token!')

        return user
