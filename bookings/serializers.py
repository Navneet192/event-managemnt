from rest_framework import serializers
from .models import  Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        models = Booking
        fields = '__all__'