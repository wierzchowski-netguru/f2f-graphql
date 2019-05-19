from django.contrib.auth import get_user_model
from django.test import TestCase

from graphene.test import Client

from v2.schema import schema

User = get_user_model()


class GraphQLV2TestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client(schema)

    def test_register(self):
        response = self.client.execute(
            '''
            mutation {
              register(input: {id: 4, username: "tymek", password: "1234"}) {
                id
                username
              }
            }
            '''
        )
        assert User.objects.filter(id=response['data']['register']['id']).exists() is True
