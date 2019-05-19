from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView

from v1.schema import schema as schema_v1
from v2.schema import schema as schema_v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/v1/', GraphQLView.as_view(graphiql=True, schema=schema_v1)),
    path('graphql/v2/', GraphQLView.as_view(graphiql=True, schema=schema_v2)),
]
