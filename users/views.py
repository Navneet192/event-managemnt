from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def register(request):
    first_name = request.data['first_name']
    email = request.data['email']
    password = request.data['password']

    if not first_name or not email or not password:
        return Response('fill all the required fields')
    if Users.objects.filter(email=email).exists():
        return Response('email already exists')
    
    user = Users.objects.create(
        first_name = first_name,
        email = email,
        password = password
    )

    return Response({"message : user registered Successfully"} , status=201)
    
@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    users = Users.objects.filter(email=email).first()
    if not users or  users.password != password:
        return Response('invalid password')
    return Response({'login successfully'} , status=200)

@api_view(['GET'])
def users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users , many=True)
    return Response(serializer.data)




