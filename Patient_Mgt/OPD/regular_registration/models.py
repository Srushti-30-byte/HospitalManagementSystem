from django.db import models
from django.utils import timezone


# Create your models here.
# Regular Registration Model
class RegularRegistration(models.Model):
    # Patient Basic Info
    REGISTRATION_TYPE_CHOICES = [
        ("new", "New Registration"),
        ("registered", "Registered"),
    ]
    registration_type = models.CharField(
        max_length=10, choices=REGISTRATION_TYPE_CHOICES, default="new"
    )

    UHID = models.CharField(
        max_length=50, unique=True, blank=True, null=True
    )  # Unique Patient ID
    PREFIX_CHOICES = [("Mr", "Mr"), ("Miss", "Miss"), ("Mrs", "Mrs")]
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES, default="Mr")
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")

    # Address Info
    address = models.TextField()
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    # Personal Information
    date_of_birth = models.DateField()
    age_years = models.IntegerField(blank=True, null=True)  # Age will be calculated
    age_months = models.IntegerField(blank=True, null=True)
    age_days = models.IntegerField(blank=True, null=True)

    blood_group = models.CharField(max_length=10, blank=True, null=True)
    id_proof = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15)

    MARITAL_STATUS_CHOICES = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Widowed", "Widowed"),
    ]
    marital_status = models.CharField(
        max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True
    )

    religion = models.CharField(max_length=50, default="Indian")
    warning = models.TextField(blank=True, null=True)

    MEDICLAIM_CHOICES = [("Yes", "Yes"), ("No", "No")]
    mediclaim = models.CharField(max_length=3, choices=MEDICLAIM_CHOICES, default="No")
    reimbursement = models.CharField(
        max_length=3, choices=MEDICLAIM_CHOICES, default="No"
    )

    occupation = models.CharField(max_length=100, blank=True, null=True)
    dependant = models.CharField(max_length=100, blank=True, null=True)
    dep_occupation = models.CharField(max_length=100, blank=True, null=True)
    provisional_diagnosis = models.TextField(blank=True, null=True)

    # Appointment Details
    visit_date = models.DateField()
    visit_time = models.TimeField(default=timezone.now)
    hospital = models.CharField(max_length=100, default="MIT Hospital")

    PATIENT_TYPE_CHOICES = [("Self", "Self"), ("Dependent", "Dependent")]
    patient_type = models.CharField(
        max_length=10, choices=PATIENT_TYPE_CHOICES, default="Self"
    )

    company = models.CharField(max_length=100, blank=True, null=True)
    tariff = models.CharField(max_length=50, default="HOSPITAL")
    DEPARTMENT_CHOICES = [
        ("neurology", "Neurology"),
        ("cardiology", "Cardiology"),
        ("gynaecology", "Gynaecology"),
        ("obstetrics", "Obstetrics"),
        ("surgery", "Surgery"),
        ("radiology", "Radiology"),
        ("gastroenterology", "Gastroenterology"),
        ("pathology", "Pathology"),
        ("pharmacy", "Pharmacy"),
        ("pediatrics", "Pediatrics"),
        ("emergency_medicine", "Emergency Medicine"),
    ]
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    doctor = models.CharField(max_length=100, blank=True, null=True)
    ref_doctor = models.CharField(max_length=100, blank=True, null=True)

    # Extra Fields
    is_vip = models.BooleanField(default=False)  # Mark VIP
    photo = models.ImageField(
        upload_to="patient_photos/", blank=True, null=True
    )  # Upload Photo

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when registered
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.UHID}"
