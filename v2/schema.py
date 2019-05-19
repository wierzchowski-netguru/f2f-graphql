import graphene

from v2.mutations import Mutation
from v2.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
