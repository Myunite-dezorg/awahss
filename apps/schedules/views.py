import requests
from datetime import datetime
from django.shortcuts import render
from apps.schedules.models.sched import Schedule, Flight, Airline, Arrival, Departure

def fetch_and_insert_flights(request):
    url = "https://app.goflightlabs.com/advanced-flights-schedules"
    params = {
        "access_key": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMmExMjFlNzNmNjBmMmNlNTNkNDk2MjMyMWVmOTc5MGEwN2ViMDAyYmI3YTJhMzI0ODBiMzU5YTYyMTYxNWQxZTBkZjI3ZjM1NWYyZTI5MTkiLCJpYXQiOjE2NzY3MDUwMzYsIm5iZiI6MTY3NjcwNTAzNiwiZXhwIjoxNzA4MjQxMDM2LCJzdWIiOiI4NDc0Iiwic2NvcGVzIjpbXX0.ar_ncouXcVA3qUqCaWh3Hx1iKHvHa7mpXn6NSGd7pw77O7WuhJIev2niVV-eOFHF8dH5xpOu_x2DE5bSwGSJkQ',
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
        schedule, _ = Schedule.objects.get_or_create(
            flight=flight,
            airline=airline,
            arrival=arrival,
            departure=departure
        )

    flights = Schedule.objects.filter(date=current_date).prefetch_related(
        'flight', 'airline', 'arrival', 'departure'
    )

    context = {'flights': flights}

    return render(request, 'flight_data.html', context)



def flight_list(request):
    url = "https://app.goflightlabs.com/advanced-flights-schedules"
    params = {
        "access_key": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMmExMjFlNzNmNjBmMmNlNTNkNDk2MjMyMWVmOTc5MGEwN2ViMDAyYmI3YTJhMzI0ODBiMzU5YTYyMTYxNWQxZTBkZjI3ZjM1NWYyZTI5MTkiLCJpYXQiOjE2NzY3MDUwMzYsIm5iZiI6MTY3NjcwNTAzNiwiZXhwIjoxNzA4MjQxMDM2LCJzdWIiOiI4NDc0Iiwic2NvcGVzIjpbXX0.ar_ncouXcVA3qUqCaWh3Hx1iKHvHa7mpXn6NSGd7pw77O7WuhJIev2niVV-eOFHF8dH5xpOu_x2DE5bSwGSJkQ',
        "iataCode": "SVO",
        "type": "departure"
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    context = {'flights': data}
    return render(request, 'flights/flight_list.html', context)