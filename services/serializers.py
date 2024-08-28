from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name_services', 'description', 'price', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']