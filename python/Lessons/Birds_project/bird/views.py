from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bird
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import BirdSerializer


# Create your views here.

# class BirdView(APIView):
#     """
#         API endpoint that allows birds to be viewed or edited.
#     """
#     def get(self,request):
#         birds = Bird.objects.all()
#         return Response({"birds":birds})


class BirdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bird.objects.all().order_by('-name')
    serializer_class = BirdSerializer

