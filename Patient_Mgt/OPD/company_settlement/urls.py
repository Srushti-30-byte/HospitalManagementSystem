from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanySettlementViewSet

# Create a router
router = DefaultRouter()
router.register(
    r"company-settlement", CompanySettlementViewSet, basename="companysettlement"
)

# Define URL patterns
urlpatterns = [
    path("", include(router.urls)),  # Include the router-generated URLs
]
