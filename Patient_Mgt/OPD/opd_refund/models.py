from django.db import models
from django.contrib.auth.models import User


class OPDRefund(models.Model):
    OPD_IPD_CHOICES = [
        ("OPD", "OPD"),
        ("IPD", "IPD"),
        ("ALL", "ALL"),
    ]

    AUTHORIZATION_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Authorized", "Authorized"),
        ("All", "All"),
    ]

    PAYMENT_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("All", "All"),
    ]

    refund_date = models.DateField()
    refund_no = models.CharField(max_length=50, unique=True)
    uhid = models.CharField(max_length=50)
    patient_name = models.CharField(max_length=255)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    opd_ipd_type = models.CharField(
        max_length=3, choices=OPD_IPD_CHOICES, default="OPD"
    )
    authorization_status = models.CharField(
        max_length=10, choices=AUTHORIZATION_STATUS_CHOICES, default="Pending"
    )
    payment_status = models.CharField(
        max_length=10, choices=PAYMENT_STATUS_CHOICES, default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Refund No: {self.refund_no} - {self.patient_name}"
