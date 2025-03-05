from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrescriptionViewSet

# Create a router and register the PrescriptionViewSet
router = DefaultRouter()
router.register(r"prescriptions", PrescriptionViewSet)

# Define the URL patterns
urlpatterns = [
    path("", include(router.urls)),
]
