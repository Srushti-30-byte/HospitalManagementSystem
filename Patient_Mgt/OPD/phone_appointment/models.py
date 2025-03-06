from django.db import models
from django.utils import timezone


# Create your models here.
class PhoneAppointment(models.Model):
    # Patient Information
    PATIENT_TYPE_CHOICES = [
        ("new", "New Patient"),
        ("registered", "Registered Patient"),
    ]
    patient_type = models.CharField(
        max_length=15, choices=PATIENT_TYPE_CHOICES)

    PREFIX_CHOICES = [
        ("Mr", "Mr"),
        ("Miss", "Miss"),
        ("Mrs", "Mrs"),
    ]
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    address = models.TextField()
    mobile_no = models.CharField(max_length=15)

    ref_doctor = models.CharField(max_length=100, blank=True, null=True)

    APPOINTMENT_TYPE_CHOICES = [
        ("patient", "Patient"),
        ("follow-up", "Follow-up"),
    ]
    appointment_type = models.CharField(
        max_length=20, choices=APPOINTMENT_TYPE_CHOICES, default="patient"
    )

    # Appointment Details
    appointment_date = models.DateField()
    appointment_time = models.TimeField(default=timezone.now)

    YES_NO_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
    ]
    appointment_given = models.CharField(
        max_length=3, choices=YES_NO_CHOICES, default="no"
    )
    appointment_kept = models.CharField(
        max_length=3, choices=YES_NO_CHOICES, default="no"
    )

    # Doctor Schedule
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
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        default="neurology",
    )

    doctor = models.CharField(max_length=100, default="Unknown Doctor")

    def __str__(self):
        return f"{self.prefix} {self.first_name} {self.last_name} - {self.appointment_date} ({self.appointment_status})"


# Express Registration Model
class ExpressRegistration(models.Model):
    # Patient Registration
    PATIENT_STATUS_CHOICES = [
        ("new", "New Registration"),
        ("registered", "Registered"),
    ]
    patient_status = models.CharField(
        max_length=15, choices=PATIENT_STATUS_CHOICES)
    uhid = models.CharField(max_length=50, blank=True,
                            null=True)  # Unique Health ID
    PREFIX_CHOICES = [
        ("Mr", "Mr"),
        ("Miss", "Miss"),
        ("Mrs", "Mrs"),
    ]
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    taluka = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    date_of_birth = models.DateField()
    use_dob = models.BooleanField(default=False)  # Checkbox for using DOB
    age_years = models.IntegerField()
    age_months = models.IntegerField()
    age_days = models.IntegerField()
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B-"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    ]
    blood_group = models.CharField(
        max_length=5, choices=BLOOD_GROUP_CHOICES, blank=True, null=True
    )
    MARITAL_STATUS_CHOICES = [
        ("single", "Single"),
        ("married", "Married"),
        ("divorced", "Divorced"),
        ("widowed", "Widowed"),
    ]
    marital_status = models.CharField(
        max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True
    )
    id_proof = models.CharField(max_length=100, blank=True, null=True)
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField(blank=True, null=True)
    weight_kg = models.FloatField(blank=True, null=True)
    height_cm = models.FloatField(blank=True, null=True)

    # Visit Details
    visit_date = models.DateField()
    visit_time = models.TimeField(default=timezone.now)
    hospital = models.CharField(max_length=100)
    PATIENT_TYPE_CHOICES = [
        ("self", "Self"),
        ("insurance", "Insurance"),
        ("corporate", "Corporate"),
    ]
    patient_type = models.CharField(
        max_length=20, choices=PATIENT_TYPE_CHOICES)
    company = models.CharField(max_length=100, blank=True, null=True)
    tariff = models.CharField(max_length=50)
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
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    doctor = models.CharField(max_length=100)
    cabin = models.CharField(max_length=50, blank=True, null=True)
    ref_doctor = models.CharField(max_length=100, blank=True, null=True)
    other_doctor = models.CharField(max_length=100, blank=True, null=True)
    provisional_diagnosis = models.TextField(blank=True, null=True)
    visit_only = models.BooleanField(default=False)
    visit_flag = models.CharField(max_length=50, blank=True, null=True)

    # Relative Details
    relative_name = models.CharField(max_length=100, blank=True, null=True)
    relative_address = models.TextField(blank=True, null=True)
    relative_phone_no = models.CharField(max_length=15, blank=True, null=True)
    RELATION_CHOICES = [
        ("father", "Father"),
        ("mother", "Mother"),
        ("spouse", "Spouse"),
        ("sibling", "Sibling"),
        ("guardian", "Guardian"),
    ]
    relation = models.CharField(
        max_length=50, choices=RELATION_CHOICES, blank=True, null=True
    )

    # Service Details
    service_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    doctor_name = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)

    # Billing
    discount_amount = models.FloatField(blank=True, null=True)
    net_amount = models.FloatField(blank=True, null=True)
    bill_remark = models.TextField(blank=True, null=True)
    payment_mode_cash = models.BooleanField(default=False)

    # Miscellaneous
    warning = models.TextField(blank=True, null=True)
    is_mlc = models.BooleanField(default=False)
    attachment = models.FileField(
        upload_to="attachments/", blank=True, null=True)

    def __str__(self):
        return f"{self.prefix} {self.first_name} {self.last_name} - {self.hospital} ({self.visit_date})"


# Phone Appointment List Model
class PhoneAppointmentList(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    doctor = models.CharField(max_length=255)
    doctor_mobile = models.CharField(max_length=15)  # New Field
    ref_doctor_name = models.CharField(max_length=255)  # New Field
    from_date = models.DateField()
    to_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    appointment_type = models.CharField(
        max_length=50,
        choices=[("OPD", "OPD"), ("IPD", "IPD"), ("Emergency", "Emergency")],
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    department = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[("Kept", "Kept"), ("Cancelled", "Cancelled"),
                 ("Pending", "Pending")],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.appointment_date}"
