from rest_framework import serializers
from .models import Users
class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email', 'password')

    def add(self , validated_data):
        user = Users.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password']
        )    
        return user
