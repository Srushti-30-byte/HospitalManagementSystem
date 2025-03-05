from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalRecordViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(
    r"medical-records", MedicalRecordViewSet, basename="medicalrecord"
)  # The URL will be `/api/medical-records/`

# Define URL patterns
urlpatterns = [
    path("", include(router.urls)),  # Include the router-generated URLs
]
