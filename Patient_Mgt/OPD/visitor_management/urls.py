from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisitorDetailsViewSet, VisitorListViewSet, VisitorPassViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r"visitor-details", VisitorDetailsViewSet, basename="visitor-details")
router.register(r"visitor-list", VisitorListViewSet, basename="visitor-list")
router.register(r"visitor-pass", VisitorPassViewSet, basename="visitor-pass")

# Define URL patterns
urlpatterns = [
    path("", include(router.urls)),
]
