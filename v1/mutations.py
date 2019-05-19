from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

import graphene
import graphql_jwt

from core.models import Post, Thread
from v1.types import PostType, UserType

User = get_user_model()


class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = User(
            username=username,
            password=make_password(password)
        )
        user.save()

        return CreateUserMutation(user=user)


class CreateThreadMutation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    first_post = graphene.Field(PostType)

    class Arguments:
        name = graphene.String()
        text = graphene.String()
        forum_id = graphene.Int()

    def mutate(self, info, name, text, forum_id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged to create a thread!')

        thread = Thread.objects.create(
            name=name,
            user=user,
            forum_id=forum_id
        )

        post = Post.objects.create(
            text=text,
            user=user,
            thread=thread
        )

        return CreateThreadMutation(
            id=thread.id,
            name=thread.name,
            first_post=post
        )


class CreatePostMutation(graphene.Mutation):
    id = graphene.Int()
    text = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        text = graphene.String()
        thread_id = graphene.Int()

    def mutate(self, info, text, thread_id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged to create a thread!')

        post = Post.objects.create(
            text=text,
            user=user,
            thread_id=thread_id
        )

        return CreatePostMutation(
            id=post.id,
            text=post.text,
            user=post.user
        )


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    register = CreateUserMutation.Field()
    create_thread = CreateThreadMutation.Field()
    create_post = CreatePostMutation.Field()
