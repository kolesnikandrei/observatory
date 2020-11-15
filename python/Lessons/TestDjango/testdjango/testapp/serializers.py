from . import models
from rest_framework import serializers


class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transmission
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):


    transmission = TransmissionSerializer

    class Meta:
        model = models.Car
        fields = '__all__'
        extra_kwargs = {'max_speed': {'required': True}}
