from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OP_patient_paymentViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(
    r"op-patient-payments", OP_patient_paymentViewSet, basename="op-patient-payment"
)

# Define URL patterns
urlpatterns = [
    path("", include(router.urls)),  # Include router-generated URLs
]
