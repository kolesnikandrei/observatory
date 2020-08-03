from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.





class BirdViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows birds to be viewed or edited.
    """