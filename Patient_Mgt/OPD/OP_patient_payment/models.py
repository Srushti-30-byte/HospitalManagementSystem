from django.db import models
from django.utils import timezone

# from . import OPDBill


# Create your models here.
class OP_patient_payment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)  # Storing as string to allow `+91`
    uhid = models.CharField(max_length=50, blank=True, null=True)  # Optional

    consulting_doctor = models.CharField(max_length=100, blank=True, null=True)

    from_date = models.DateField()
    to_date = models.DateField()

    PATIENT_TYPE_CHOICES = [
        ("OPD", "Outpatient"),
        ("ER", "Emergency"),
        ("IPD", "Inpatient"),
    ]
    patient_type = models.CharField(max_length=10, choices=PATIENT_TYPE_CHOICES)

    advance_search = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("printed", "Printed"),
        ("pending", "Pending"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp for record creation

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.patient_type}"
