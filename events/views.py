from django.shortcuts import render
from .models import Events 
from rest_framework import viewsets
from .serializers import EventsSerializer
from rest_framework.response import Response
from rest_framework import status

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


    def list(self , request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset , many=True)
        return Response(serializer.data)
    
    def create(self , request):
        event_name = request.data.get('event_name')
        event_date = request.data.get('event_date')
        event_time = request.data.get('event_time')
        event_location = request.data.get('event_location')
        if Events.objects.filter(event_name=event_name , event_date=event_date , event_time=event_time , event_location=event_location).exists():
            return Response({'message' : 'Event already exists.'} , status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status = 201)
            return Response(serializer.errors , status=400)

    def retrieve(self , request , pk=None):
        queryset = self.get_queryset()
        event_category = request.query_params.get('event_category' , None)
        if pk and  pk.isdigit():
            event = queryset.filter(pk=pk).first()
            if event:
                serializer = self.get_serializer(event)
                return Response(serializer.data)
            else:
                return Response({'message' : 'Event not found'} , status=400)
        if event_category or pk:
            category = event_category if event_category else pk
            event = queryset.filter(event_category=category)
            if event.exists():
                serializer = self.get_serializer(event , many=True)
                return Response(serializer.data)
            else:
                return Response({'message' : 'Event not found'} , status=400)
        return Response({'message' : 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self , request , pk=None):
        queryset = self.get_queryset()
        event = queryset.filter(pk=pk).first()
        if event:
            event.delete()
            return Response({'Message' : 'Event deleted successfully.' } , status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message' : 'Event not found'} , status=status.HTTP_404_NOT_FOUND)
        


        




    

