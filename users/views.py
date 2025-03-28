from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer

class viewList():
    Users = Users.objects.all()
    serializers = UsersSerializer(Users, many=True)
    




