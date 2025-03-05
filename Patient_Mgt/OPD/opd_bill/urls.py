from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OPDBillViewSet  # ✅ Ensure correct import

# Create a router and register the OPDBill viewset
router = DefaultRouter()
router.register(
    r"opd-bills", OPDBillViewSet, basename="opdbill"
)  # ✅ API URL will be `/api/opd-bills/`

# Define URL patterns
urlpatterns = [
    path("", include(router.urls)),  # ✅ Ensures correct API URL
]
