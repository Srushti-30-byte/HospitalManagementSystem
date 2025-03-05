from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowupListViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r"followup-list", FollowupListViewSet, basename="followup-list")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
