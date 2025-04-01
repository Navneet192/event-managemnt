from users.models import Users
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Booking
from events.models import Events


@api_view(['POST'])
def book_event(request):
    email = request.data.get('email')
    event_name = request.data.get('event_name')
    event_date = request.data.get('event_date')
    event_location = request.data.get('event_location')
    num_tickets = int(request.data.get('num_tickets'))

    try:
        event = Events.objects.filter(event_name = event_name , event_date = event_date , event_location = event_location)
        if not event.exists():
            return Response('Event not found')
        if event.count() > 1:
            return Response('Multiple events found')
        event = event.first()

    except Events.DoesNotExist:
        return Response('Event not found')
    
    total_price = event.event_price * num_tickets
    if event.event_capacity < num_tickets:
        return Response('Sorry you are late Ticket not available')
    
    try:
        user = Users.objects.get(email=email)
    except Users.DoesNotExist:
        return Response("User not found")    
    
    booking = Booking.objects.create(
        user = user,
        events = event,
        num_tickets = num_tickets,
        total_price = total_price
    )
    event.event_capacity -= num_tickets
    event.save()
    return Response({
        'message' : "Booking Confirm",
        'booking_details' : {
            'user' : user.email,
            'user_name' : f'{user.first_name} {user.last_name}',
            'event_name' : event.event_name,
            'event_location' : event.event_location,
            'event_date' : event.event_date,
            'num_tickets' : num_tickets,
            'total_price' : total_price,
            'event_time' : event.event_time
        }
        }, status=201)

@api_view(['GET'])
def bookings(request):
    bookings = Booking.objects.all()
    booked_event = [] 
    for booking in bookings:
        booked_event.append({
            'booking_id' : booking.id,
            'user' : booking.user.email,
            'event_name' : booking.events.event_name,
            'event_location' : booking.events.event_location,
            'event_date' : booking.events.event_date,
            'event_time' : booking.events.event_time,
            'num_tickets': booking.num_tickets,
            'total_price' : booking.total_price
        }) 
    return Response(booked_event, status=200)
          
