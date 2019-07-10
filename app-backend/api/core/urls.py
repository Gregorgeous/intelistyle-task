from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GarmentViewSet

router = DefaultRouter()
router.register(r'garments', GarmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]