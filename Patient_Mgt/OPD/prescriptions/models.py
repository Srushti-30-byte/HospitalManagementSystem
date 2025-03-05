from django.db import models


# Create your models here.
class Prescription(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    uhid = models.CharField(max_length=50, blank=True, null=True)  # Unique Health ID

    prescription_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()

    drug_name = models.CharField(max_length=255, blank=True, null=True)
    doctor_name = models.CharField(max_length=255)
    remark = models.TextField(blank=True, null=True)

    total_count = models.PositiveIntegerField(
        default=0
    )  # Total number of prescribed items

    def __str__(self):
        return f"{self.prescription_date} - {self.first_name} {self.last_name} - {self.total_count}"
