from rest_framework import serializers
from .models import Bird




#class BirdSerializer(serializers.ModelSerializer):
class BirdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bird
        fields = ['species','name','color', 'body_length','wingspan']