import os
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from .models import Car


UNKNOWN_APP_VERSION = "1.1.1"


class GetAppVersion(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            with open(os.path.join(settings.BASE_DIR, '../VERSION.txt'), 'r') as f:
                data = {
                    'version': f.readline().rstrip('\n')
                }
        except FileNotFoundError:
            data = {
                'version': UNKNOWN_APP_VERSION
            }
        return Response(data=data, status=status.HTTP_200_OK)


class CarViewSet(viewsets.ModelViewSet):

    queryset = Car.objects.all()
