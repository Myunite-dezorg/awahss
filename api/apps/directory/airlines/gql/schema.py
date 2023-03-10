import graphene
from graphene_django import DjangoObjectType
from apps.directory.models.airline import Airline




  
class AirlineType(DjangoObjectType):
    def resolve_arl_logo(self, info):
        """Resolve product image absolute path"""
        if self.arl_logo:
            self.arl_logo = info.context.build_absolute_uri(self.arl_logo.url)
        return self.arl_logo
    class Meta:
        model = Airline


class Query(graphene.ObjectType):
    get_airlines = graphene.List(AirlineType)
   
   
    def resolve_get_airlines(root, info):
        return (
            Airline.objects.all()
        )
       


schema = graphene.Schema(query=Query)