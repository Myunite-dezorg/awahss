import requests
import json
import pandas as pd
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from apps.schedules.models.flight_sched_model import Schedule, Airline, Arrival, Departure, Flight

# def fetch_flight_data(request):
#     access_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMmExMjFlNzNmNjBmMmNlNTNkNDk2MjMyMWVmOTc5MGEwN2ViMDAyYmI3YTJhMzI0ODBiMzU5YTYyMTYxNWQxZTBkZjI3ZjM1NWYyZTI5MTkiLCJpYXQiOjE2NzY3MDUwMzYsIm5iZiI6MTY3NjcwNTAzNiwiZXhwIjoxNzA4MjQxMDM2LCJzdWIiOiI4NDc0Iiwic2NvcGVzIjpbXX0.ar_ncouXcVA3qUqCaWh3Hx1iKHvHa7mpXn6NSGd7pw77O7WuhJIev2niVV-eOFHF8dH5xpOu_x2DE5bSwGSJkQ'
    
#     # Make a HTTP GET request to the API endpoint

#     response = requests.get(f'https://app.goflightlabs.com/advanced-flights-schedules?access_key={access_key}')
    
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the response to get the flight data
#         flight_data = response.json()
#         # print(flight_data)
        

#         # Create a new Flight instance with the retrieved flight data
#         # for schedule in flight_data:
#         #  Schedule.objects.create(
#         #     # id=schedule['id'],
#         #     status=flight_data.get('status', ''),
#         #     type=flight_data.get('type', ''),
#         # ),
        
#         schedule_data = {
            
#              'status': flight_data.get('status'),
#              'type': flight_data.get('type', ''),
#         },
#         schedule, created = Schedule.objects.get_or_create(**schedule_data)
#         for airline in flight_data:
#           Airline.objects.create(
#             iataCode=flight_data.get('iataCode', ''),
#             icaoCode=flight_data.get('icaoCode', ''),
#             name=flight_data.get('name', ''),
#             schedule=schedule,
#         ),
#         # airline.save()
#         for arrival in flight_data:
#          Arrival.objects.create(
#             actualRunway=flight_data.get('actualRunway'),
#             actualTime=flight_data.get('actualTime'),
#             baggage=flight_data.get('baggage'),
#             delay=flight_data.get('delay'),
#             estimatedRunway=flight_data.get('estimatedRunway'),
#             estimatedTime=flight_data.get('estimatedTime'),
#             gate=flight_data.get('gate'),
#             iataCode=flight_data.get('iataCode'),
#             icaoCode=flight_data.get('icaoCode'),
#             scheduledTime=flight_data.get('scheduledTime'),
#             terminal=flight_data.get('terminal'),
#             chedule=schedule,
#         ),
#         # arrival.save()
#         for departure in flight_data:
#          Departure.objects.create(
#             actualRunway=flight_data.get('actualRunway'),
#             actualTime=flight_data.get('actualTime'),
#             baggage=flight_data.get('baggage'),
#             delay=flight_data.get('delay'),
#             estimatedRunway=flight_data.get('estimatedRunway'),
#             estimatedTime=flight_data.get('estimatedTime'),
#             gate=flight_data.get('gate'),
#             iataCode=flight_data.get('iataCode'),
#             icaoCode=flight_data.get('icaoCode'),
#             scheduledTime=flight_data.get('scheduledTime'),
#             terminal=flight_data.get('terminal'),
#             chedule=schedule,
#         ),
#         # departure.save()
#         for flight in flight_data:
#          Flight.objects.create(
#             iataNumber=flight_data.get('iataNumber'),
#             icaoNumber=flight_data.get('icaoNumber'),
#             name=flight_data.get('number'),
#             chedule=schedule,

#         ),
#         # flight.save()
        



#         # Render a template to show that the flight data has been fetched and saved
#         return render(request, 'flight_data.html', {
#             'schedule': schedule,
#             'airline': airline,
#             'arrival': arrival,
#             'departure': departure,
#             'flight': flight
#             })
#     else:
#         # Handle the error
#         return render(request, 'error.html', {'status_code': response.status_code})


def fetch_and_insert_flights(request):
    url = "https://app.goflightlabs.com/advanced-flights-schedules"
    params = {
        "access_key": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMmExMjFlNzNmNjBmMmNlNTNkNDk2MjMyMWVmOTc5MGEwN2ViMDAyYmI3YTJhMzI0ODBiMzU5YTYyMTYxNWQxZTBkZjI3ZjM1NWYyZTI5MTkiLCJpYXQiOjE2NzY3MDUwMzYsIm5iZiI6MTY3NjcwNTAzNiwiZXhwIjoxNzA4MjQxMDM2LCJzdWIiOiI4NDc0Iiwic2NvcGVzIjpbXX0.ar_ncouXcVA3qUqCaWh3Hx1iKHvHa7mpXn6NSGd7pw77O7WuhJIev2niVV-eOFHF8dH5xpOu_x2DE5bSwGSJkQ",
        "iataCode": "SVO",
        "type": "departure"
    }
    response = requests.get(url, params=params)
    data = response.json()
    current_date = datetime.today().date()

    schedule = Schedule.objects.create(date=current_date)

    for flight_data in data["data"]:
        airline_data = flight_data["airline"]
        airline, _ = Airline.objects.get_or_create(
            iataCode=airline_data["iataCode"],
            schedule=schedule,
            defaults={
                "icaoCode": airline_data["icaoCode"],
                "name": airline_data["name"]
            }
        )
        arrival_data = flight_data["arrival"]
        arrival, _ = Arrival.objects.get_or_create(
            iataCode=arrival_data["iataCode"],
            defaults={
                "icaoCode": arrival_data["icaoCode"]
            }
        )
        departure_data = flight_data["departure"]
        departure, _ = Departure.objects.get_or_create(
            iataCode=departure_data["iataCode"],
            defaults={
                "icaoCode": departure_data["icaoCode"]
            }
        )
        flight_data = flight_data["flight"]
        flight, _ = Flight.objects.get_or_create(
            number=flight_data["number"],
            defaults={
                "iataNumber": flight_data["iataNumber"],
                "icaoNumber": flight_data["icaoNumber"],
                "number": flight_data["number"],
            }
        )
        # status_data = flight_data
        schedule, _ = Schedule.objects.get_or_create(
            # status=status_data["status"],
            # type=status_data["type"],
            flight=flight,
            airline=airline,
            arrival=arrival,
            # schedule=schedule,
            departure=departure
        )
        context = {'message': 'Flights data has been fetched and inserted successfully!'}
    else:
        context = {'message': 'Failed to fetch flights data! Please try again later.'}

    return render(request, 'flight_data.html', context)
  
