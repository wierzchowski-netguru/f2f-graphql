from django.contrib.auth import get_user_model

import graphene
import graphql_jwt
from graphene_django.rest_framework.mutation import SerializerMutation

from core.serializers import UserSerializer

User = get_user_model()


class CreateUserMutation(SerializerMutation):
    class Meta:
        serializer_class = UserSerializer
        model_operations = ['create']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    register = CreateUserMutation.Field()
