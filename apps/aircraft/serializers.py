from rest_framework import routers, serializers, viewsets
from .models import Aircraft

class AcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = [
        'pk',
        'iata_code',
        'icao_code',
        'rus_name',
        'comment',
        'comment_rus',
        'public_name_eng',
        'public_name_rus'
        ]