from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VaccinationViewSet

router = DefaultRouter()
router.register(r"vaccination", VaccinationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
