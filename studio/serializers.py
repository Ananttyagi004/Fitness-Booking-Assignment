from rest_framework import serializers
from .models import FitnessClass, Booking

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class_name = serializers.CharField(source='fitness_class.name', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'client_name', 'client_email', 'class_name']


class BookingCreateSerializer(serializers.Serializer):
    class_id = serializers.IntegerField()
    client_name = serializers.CharField()
    client_email = serializers.EmailField()
