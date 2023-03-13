import os
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from apps.directory.models.airline import Airline

class LinkAirlineImagesView(View):
    def get(self, request):
        # Get all Airline records that don't have an image set
        airlines_without_image = Airline.objects.filter(arl_logo__isnull=True)

        # Loop through each record and set the image field to the appropriate image
        for airline in airlines_without_image:
            iata_code = airline.iata_code
            image_name = iata_code + '.png'
            image_path = os.path.join(settings.MEDIA_ROOT, 'airlines/square', image_name)
            if os.path.exists(image_path):
                airline.arl_logo = 'airlines/square/' + image_name
                airline.save()

        return HttpResponse('Airline images linked successfully.')