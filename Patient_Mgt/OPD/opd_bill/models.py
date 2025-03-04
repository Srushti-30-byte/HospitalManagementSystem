from django.db import models


# Create your models here.
# OPD Bill Model
class OPDBill(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    uhid = models.CharField(max_length=50, unique=True)  # Unique Health ID
    consulting_doctor = models.CharField(max_length=100)

    from_date = models.DateField()
    to_date = models.DateField()

    PATIENT_TYPE_CHOICES = [
        ("OPD", "Out-Patient Department"),
        ("IPD", "In-Patient Department"),
        ("ER", "Emergency Room"),
    ]
    patient_type = models.CharField(max_length=10, choices=PATIENT_TYPE_CHOICES)

    advanced_search_option = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.uhid})"
