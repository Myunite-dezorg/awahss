from import_export import resources
from .models import Aircraft

class AircraftResource(resources.ModelResource):
    class Meta:
        model = Aircraft