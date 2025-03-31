from rest_framework import serializers
from .models import Events , Booking , Ticket
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Events
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        models = Booking
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        models = Ticket
        fields = '__all__'