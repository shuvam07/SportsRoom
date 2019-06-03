from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserProfileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'#('username', 'email', 'id')