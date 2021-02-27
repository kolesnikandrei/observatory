from . import models
from rest_framework import serializers
from django.db import transaction


def extra_kwargs_factory(fields, **options):
    return {k: options for k in fields}


class TransmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transmission
        fields = '__all__'


class CarInputSerializer(serializers.ModelSerializer):

    # transmission = TransmissionSerializer()

    def validate(self, attrs):
        print(attrs)

    def validate_max_speed(self, max_speed_value):
        if max_speed_value < 40 or max_speed_value > 500:
            raise serializers.ValidationError('max_speed should be in range 40...500')
        return max_speed_value

    class Meta:
        model = models.Car

        required_fields = (
            'name',
            'max_speed',
            'engine_type',
        )

        optional_fields = (
            'transmission',
        )

        extra_kwargs = extra_kwargs_factory(required_fields, required=True, allow_null=False)
        extra_kwargs.update(
            extra_kwargs_factory(optional_fields, required=False)
        )
        fields = required_fields + optional_fields + ('id',)

    # def create(self, validated_data):
    #     print(validated_data)
    #     transmission = validated_data.pop('transmission')
    #
    #     return models.Car.objects.create(
    #         transmission=models.Transmission.objects.create(**transmission),
    #         **validated_data,
    #     )
    #
    # def _update_transmission(self,instance, transmission ):
    #     if transmission:
    #         transmission_serializer = self.fields['transmission']
    #         instance.transmission = transmission_serializer.update(instance.transmission, transmission)
    #
    # def update(self, instance, validated_data):
    #     transmission = validated_data.pop('transmission', None)
    #     with transaction.atomic():
    #         self._update_transmission(instance, transmission)
    #         updated_instance = super().update(instance, validated_data)
    #
    #     return updated_instance


class CarOutputSerializer(CarInputSerializer):

    transmission = TransmissionSerializer()


class CarSerializer(CarInputSerializer):

    def to_representation(self, instance):
        return CarOutputSerializer(instance=instance).data
