from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bird


# Create your views here.

class BirdView(APIView):
    """
        API endpoint that allows birds to be viewed or edited.
    """
    def get(self,request):
        birds = Bird.objects.all()
        return Response({"birds":birds})