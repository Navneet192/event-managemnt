from rest_framework import serializers

from .models import Users
class UsersSerializer(serializers.ModelSerializers):
    class Meta:
        model = Users
        fields = '__all__'
        
