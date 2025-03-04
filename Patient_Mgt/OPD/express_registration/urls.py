from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpressRegistrationViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r"express-registrations", ExpressRegistrationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
