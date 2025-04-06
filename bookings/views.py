from .models import  Booking
from .serializers import BookingSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from events.models import Events


class bookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer   

    def list(self , request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset , many=True)
        return Response(serializer.data)
    
    def create(self , request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking =  serializer.save()
        try:
            event = Events.objects.get(id=booking.event_id)
        except Events.DoesNotExist:
            return Response({'error' : 'Event not found'} , status=404)
        if booking.num_tickets > event.event_capacity:
            return Response({
                'error':'Not enough tickets availabe',
                'available_capacity' : event.event_capacity,
            } , status=400)
        
        if booking.num_tickets <= 0:  
            return Response({
                'error':'Number of tickets should be greater than 0',
            } , status=400)
        
        event.event_capacity -= booking.num_tickets
        event.save()

        response_data = {
            'message': 'Booking created successfully',
            'booking_details': {
                'id': booking.id,
                'event_name': event.event_name,
                'event_location': event.event_location,
                'event_date': event.event_date,
                'contact_email': booking.contact_email,
                'contact_phone': booking.contact_phone,
                'num_tickets': booking.num_tickets,
                'total_price': event.event_price * booking.num_tickets,
        }
        }
        return Response(response_data , status=201)
    
     






    
