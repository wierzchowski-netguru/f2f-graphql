import graphene

from v1.mutations import Mutation
from v1.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
