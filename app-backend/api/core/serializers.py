from rest_framework import serializers
from .models import Garment 

class GarmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garment
        fields = ("id", "name", "description", "picture")