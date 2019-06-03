from rest_framework import serializers
from .models import *

class EquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        fields= '__all__'

class EquipmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentRequest
        fields= '__all__'