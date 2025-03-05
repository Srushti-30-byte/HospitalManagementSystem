from django.db import models


# Create your models here.
# Courier List Models
class CourierList(models.Model):
    COURIER_TYPE_CHOICES = [
        ("Inward", "Inward"),
        ("Outward", "Outward"),
    ]

    CATEGORY_CHOICES = [
        ("Personal", "Personal"),
        ("Company", "Company"),
    ]

    courier_date = models.DateField()
    person_company_name = models.CharField(max_length=255)
    courier_type = models.CharField(
        max_length=7, choices=COURIER_TYPE_CHOICES
    )  # Inward / Outward
    category = models.CharField(
        max_length=8, choices=CATEGORY_CHOICES
    )  # Personal / Company
    address = models.TextField()
    contact_no = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.person_company_name} - {self.courier_type} ({self.courier_date})"


# Courier Details Model
class CourierDetails(models.Model):
    date = models.DateField()
    time = models.TimeField()
    inward_outward = models.CharField(
        max_length=10, choices=[("Inward", "Inward"), ("Outward", "Outward")]
    )
    personal_company = models.CharField(
        max_length=10, choices=[("Personal", "Personal"), ("Company", "Company")]
    )
    received_from = models.CharField(max_length=255)
    address = models.TextField()
    contact_no = models.CharField(max_length=15)
    courier_content = models.TextField()  # Content of Courier
    to_department = models.CharField(max_length=100)
    staff_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.received_from} - {self.inward_outward} ({self.date})"
