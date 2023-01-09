from rest_framework import serializers
from apps.flight_schedule.models import FlightTask
from apps.directory.models import Register, Airline, Station




class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    airline = serializers.StringRelatedField(many=False)
    registration = serializers.StringRelatedField(many=False)
    route = serializers.StringRelatedField(many=False)
    class Meta:
        fields = (
            'id',
            'user',
            'task_date',
            'technology',
            'airline',
            'registration',
            'flight',
            'sched_time',
            'route',
            'payload',
            'description',
            'status',
            'slug',
            'create_at',
            'update_at',
            
        )
        model = FlightTask
        
        def get_sched_time(self, obj):
            return obj.create_at.strftime("%d-%m-%Y, %H:%M")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'number',
            'ac_type',
            'co',
            'mod',
            'g_type',
            'description'

        )
        model = Register

class AirlineSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(required=False)
    class Meta:
        fields = (
            'iata',
            'icao',
            'rus_code',
            'comment_eng',
            'comment_rus',
            'country',
            'alliance',
            'lowcost',
            'description',
            'logo',

        )    

        model = Airline

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'iata',
            'icao',
           
        )    

        model = Station
