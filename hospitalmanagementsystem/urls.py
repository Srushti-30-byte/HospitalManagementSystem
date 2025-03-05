"""
URL configuration for hospitalmanagementsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hospital Management System API",
        default_version="v1",
        description="API documentation for managing hospital management system",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("Patient_Mgt.OPD.phone_appointment.urls")),
    path("api/", include("Patient_Mgt.OPD.express_registration.urls")),
    path("api/", include("Patient_Mgt.OPD.regular_registration.urls")),
    path("api/", include("Patient_Mgt.OPD.queue_management.urls")),
    path("api/", include("Patient_Mgt.OPD.medical_records.urls")),
    path("api/", include("Patient_Mgt.OPD.opd_bill.urls")),
    path("api/", include("Patient_Mgt.OPD.OP_patient_payment.urls")),
    path("api/", include("Patient_Mgt.OPD.company_settlement.urls")),
    path("api/", include("Patient_Mgt.OPD.bill_refund.urls")),
    path("api/", include("Patient_Mgt.OPD.opd_refund.urls")),
    path("api/", include("Patient_Mgt.OPD.prescriptions.urls")),
    path("api/", include("Patient_Mgt.OPD.followup_list.urls")),
    path("api/", include("Patient_Mgt.OPD.visitor_management.urls")),
    path("api/", include("Patient_Mgt.OPD.courier_management.urls")),
    path("api/", include("Patient_Mgt.OPD.vaccination.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
