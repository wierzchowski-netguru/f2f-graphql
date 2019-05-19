from django.contrib.auth import get_user_model
from django.test import TestCase

from graphene.test import Client

from v1.schema import schema

User = get_user_model()


class GraphQLV1TestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client(schema)

    def test_register(self):
        response = self.client.execute(
            '''
            mutation {
              register (username: "kazik", password: "1234") {
                user {
                  id
                  username
                  isStaff
                }
              }
            }
            '''
        )
        assert User.objects.filter(id=response['data']['register']['user']['id']).exists() is True
