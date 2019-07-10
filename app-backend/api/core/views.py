from rest_framework import viewsets
from .serializers import GarmentSerializer  
from .models import Garment
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class GarmentViewSet(viewsets.ModelViewSet):
    serializer_class = GarmentSerializer
    queryset = Garment.objects.all().order_by('id')
    permission_classes = [IsAuthenticatedOrReadOnly]


