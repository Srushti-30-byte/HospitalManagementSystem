from django.db import models


# Create your models here.
class FollowUpList(models.Model):
    seq_no = models.AutoField(primary_key=True)
    followup_date = models.DateField()
    doctor_name = models.CharField(max_length=255)
    patient_first_name = models.CharField(max_length=255)
    patient_last_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    remark = models.TextField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    phone_appointment = models.BooleanField(
        default=False
    )  # Checkbox for phone appointment
    followup_call_details = models.TextField(
        blank=True, null=True
    )  # Additional details for follow-up calls

    def __str__(self):
        return f"{self.seq_no} - {self.patient_first_name} {self.patient_last_name} - {self.doctor_name}"
