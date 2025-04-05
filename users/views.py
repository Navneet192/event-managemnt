from django.shortcuts import render
from .models import Users
from rest_framework import viewsets
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def list(self , request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self , request):
        email = request.data.get('email')
        if Users.objects.filter(email=email).exists():
            return Response({'error' : 'Email already exists try with different email'} , status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    




    





