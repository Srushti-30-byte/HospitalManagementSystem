from django.db import models

# Create your models here.


class Vaccination(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    uhid = models.CharField(max_length=50, unique=True)  # Unique Health ID
    consulting_doctor = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    patient_type = models.CharField(
        max_length=50,
        choices=[("OPD", "OPD"), ("IPD", "IPD"), ("Emergency", "Emergency")],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.uhid}"
