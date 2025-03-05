from django.db import models


class BillRefund(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    uhid = models.CharField(max_length=50, blank=True, null=True)  # Unique Hospital ID

    consulting_doctor = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    patient_type = models.CharField(
        max_length=50, choices=[("OPD", "OPD"), ("IPD", "IPD")]
    )

    advance_search_option = models.TextField(blank=True, null=True)

    status_choices = [
        ("Completed", "Completed"),
        ("Printed", "Printed"),
        ("Pending", "Pending"),
        ("Refunded", "Refunded"),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default="Pending")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.uhid}"
