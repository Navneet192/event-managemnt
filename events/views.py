from django.shortcuts import render
from .models import Events , Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create_event(request):
    event_name = request.data['event_name']
    event_category = request.data['event_category']
    event_date = request.data['event_date']
    event_time = request.data['event_time']
    event_capacity = request.data['event_capacity']
    event_price = request.data['event_price']
    event_location = request.data['event_location']
    
    if not event_name  or not event_location or not event_category:
        return Response('All fields are Required')
    if Events.objects.filter(event_name = event_name , event_location = event_location , event_date = event_date , event_time = event_time).exists():
        return Response('Event already exists')
    event = Events.objects.create(
        event_name = event_name,
        event_category = event_category,
        event_date = event_date,
        event_time = event_time,
        event_capacity = event_capacity,
        event_price = event_price,
        event_location = event_location
    )

    return Response({'message' : 'Event Created Successully' , 'event_id' : event.id} , status=201)

@api_view(['GET'])
def events(request):
    events = Events.objects.all()
    data = []
    for event in events:
        data.append({
            'event_id' : event.id,
            'event_name' : event.event_name,
            'event_category': event.event_category,
            'event_date' : event.event_date,
            'event_time' : event.event_time,
            'event_capacity' : event.event_capacity,
            'event_location' : event.event_location,
            'event_price' : event.event_price  
        })
    return Response(data)

@api_view(['PUT'])
def update_event(request):
    event_name = request.data['event_name']
    event_category = request.data['event_category']
    event_price = request.data['event_price']
    event_location = request.data['event_location']
    event_capacity = request.data['event_capacity']
    event_time = request.data['event_time']
    event_date = request.data['event_date']

    return Response('Event Updated Successfully')

@api_view(['DELETE'])
def delete_event(request):
    event_id = request.data['event_id']
    event = Events.objects.get(id = event_id)
    event.delete()
    return Response('Event Deleted Successfully')


@api_view(['POST'])
def book_event(request):
    event_name = request.data['event_name']
    num_tickets = request.data['num_tickets']
    event_id = request.data['event_id']
    user = request.user

    try:
        event = Events.objects.get(event_name = event_name)
    except Events.DoesNotExist:
        return Response('Event not found')
    
    total_price = event.event_price * num_tickets
    if event.event_capacity < num_tickets:
        return Response('Ticket not available')
    
    booking = Booking.objects.create(
        user = user,
        events = event,
        id = event_id,
        num_tickets = num_tickets,
        total_price = total_price
    )
    event.event_Capacity -= num_tickets
    event.save()
    return Response('Booking Successfull')



