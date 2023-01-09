import graphene
from graph import queries


schema = graphene.Schema(query=queries.Query)
