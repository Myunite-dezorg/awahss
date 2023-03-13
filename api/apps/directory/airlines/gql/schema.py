import graphene
from django_filters import FilterSet
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from apps.directory.models.airline import Airline

class AirlineFilter(FilterSet):
    class Meta:
        model = Airline
        fields = [
            'codeIataAirline',
            'codeIcaoAirline',
            'iataPrefixAccounting',
        ]
        filter_fields = {
            'codeIataAirline': ['exact', 'icontains'],
            'codeIcaoAirline': ['exact', 'icontains'],
            'iataPrefixAccounting': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )


  
class AirlineType(DjangoObjectType):
    def resolve_arl_logo(self, info):
        """Resolve product image absolute path"""
        if self.arl_logo:
            self.arl_logo = info.context.build_absolute_uri(self.arl_logo.url)
        return self.arl_logo
    class Meta:
        model = Airline
        interfaces = (graphene.relay.Node,)
        filterset_class = AirlineFilter
        fields = '__all__'


class Query(graphene.ObjectType):
    airlines = DjangoFilterConnectionField(AirlineType)
       


schema = graphene.Schema(query=Query)