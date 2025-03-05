from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourierListViewSet, CourierDetailsViewSet

router = DefaultRouter()
router.register(r"courier-list", CourierListViewSet)
router.register(r"courier-details", CourierDetailsViewSet)
urlpatterns = [
    path("", include(router.urls)),  # Include the router URLs
]
