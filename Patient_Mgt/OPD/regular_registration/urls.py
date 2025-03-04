from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegularRegistrationViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r"regular-registrations", RegularRegistrationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
