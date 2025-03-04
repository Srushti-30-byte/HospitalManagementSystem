from django.db import models
from django.utils import timezone


# Create your models here.
# Queue Management Model
class QueueManagement(models.Model):
    visit_time = models.DateTimeField(default=timezone.now)
    patient_name = models.CharField(max_length=255)
    cabin_number = models.CharField(max_length=50, blank=True, null=True)

    DEPARTMENT_CHOICES = [
        ("General Medicine", "General Medicine"),
        ("Cardiology", "Cardiology"),
        ("Neurology", "Neurology"),
        ("Orthopedics", "Orthopedics"),
        ("Pediatrics", "Pediatrics"),
        ("Gynecology", "Gynecology"),
        ("Dermatology", "Dermatology"),
        ("ENT", "ENT"),
        ("Ophthalmology", "Ophthalmology"),
        ("Psychiatry", "Psychiatry"),
        ("Urology", "Urology"),
        ("Oncology", "Oncology"),
        ("Radiology", "Radiology"),
        ("Pulmonology", "Pulmonology"),
        ("Nephrology", "Nephrology"),
    ]

    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    doctor_name = models.CharField(max_length=255)
    ref_doctor_name = models.CharField(max_length=255, blank=True, null=True)

    APPOINTMENT_TYPE_CHOICES = [
        ("Phone Appointment", "Phone Appointment"),
        ("Walk-in Patient", "Walk-in Patient"),
        ("Mobile App Appointment", "Mobile App Appointment"),
    ]

    appointment_type = models.CharField(max_length=50, choices=APPOINTMENT_TYPE_CHOICES)

    is_called = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient_name} - {self.department} - {self.doctor_name}"
