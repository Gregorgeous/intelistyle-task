from rest_framework import viewsets
from .serializers import GarmentSerializer  
from .models import Garment
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class GarmentViewSet(viewsets.ModelViewSet):
    serializer_class = GarmentSerializer
    queryset = Garment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class searchListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = GarmentSerializer
    def get_queryset(self):
        queryset = Garment.objects.all()
        search_query = self.request.query_params.get('q', None)
        if search_query is not None:
            queryset = queryset.search(query=search_query)
        return queryset

