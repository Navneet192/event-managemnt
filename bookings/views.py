from .models import  Booking
from .serializers import BookingSerializer
from rest_framework import viewsets


class bookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer    

    
