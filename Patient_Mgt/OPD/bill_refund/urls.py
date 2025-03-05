from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BillRefundViewSet

# Create a router and register the BillRefund viewset
router = DefaultRouter()
router.register(r"bill-refunds", BillRefundViewSet, basename="billrefund")

# URL patterns
urlpatterns = [
    path("", include(router.urls)),
]
