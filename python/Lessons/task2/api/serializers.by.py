from django.contrib.auth.models import Bird
from rest_framework import serializers




class BirdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bird
        fields = ['species','name','color', 'body_length','wingspan']