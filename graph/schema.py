import graphene
from graph import queries
import api.apps.ibase.gql.schema as imsgcodes 
import api.apps.directory.airlines.gql.schema as airlines



class Query(imsgcodes.Query, airlines.Query):
    pass

schema = graphene.Schema(query=Query)
