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
    num_tickets = int(request.data.get('num_tickets'))

    try:
        event = Events.objects.filter(event_name = event_name)
        if not event.exists():
            return Response('Event not found')
        if event.count() > 1:
            return Response('Multiple events found')
        event = event.first()

    except Events.DoesNotExist:
        return Response('Event not found')
    
    total_price = event.event_price * num_tickets
    if event.event_capacity < num_tickets:
        return Response('Ticket not available')
    
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
    return Response('Booking Successfull')
