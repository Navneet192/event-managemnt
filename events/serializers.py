from rest_framework import serializers
from .models import Events  , Ticket
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Events
        fields = '__all__'
