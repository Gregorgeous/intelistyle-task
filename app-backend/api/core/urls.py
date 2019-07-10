from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GarmentViewSet, searchListView

router = DefaultRouter()
router.register(r'garments', GarmentViewSet)
router.register(r'search', searchListView, basename="search")

urlpatterns = [
    path("", include(router.urls)),
]