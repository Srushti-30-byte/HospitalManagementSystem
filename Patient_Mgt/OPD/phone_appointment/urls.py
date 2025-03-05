from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhoneAppointmentViewSet, PhoneAppointmentListViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r"phone-appointments", PhoneAppointmentViewSet)
router.register(r"phone-appointments-list", PhoneAppointmentListViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
