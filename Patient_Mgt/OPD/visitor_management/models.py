from django.db import models


# Create your models here.
# Visitor Details Model
class VisitorDetails(models.Model):
    VISITOR_TYPE_CHOICES = [
        ("new", "New Visitor"),
        ("existing", "Existing Visitor"),
    ]

    PREFIX_CHOICES = [
        ("Mr", "Mr"),
        ("Miss", "Miss"),
        ("Mrs", "Mrs"),
        ("Dr", "Dr"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    MEETING_REASON = [
        ("Software Demo", "Software Demo"),
        ("Doctor Meeting", "Doctor Meeting"),
        ("Documentation Meet", "Documentation Meet"),
        ("Equipment Demo", "Equipment Demo"),
        ("Camp Meeting", "Camp Meeting"),
    ]

    visitor_type = models.CharField(
        max_length=10, choices=VISITOR_TYPE_CHOICES, default="new"
    )
    visit_date = models.DateField()
    in_time = models.TimeField()
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField(blank=True, null=True)
    visitor_card = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to="visitor_photos/", blank=True, null=True)

    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    appointment_taken = models.BooleanField(default=False)
    meeting_reason = models.CharField(
        max_length=40, choices=MEETING_REASON, default="Doctor Meeting"
    )
    visitor_blacklisted = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)
    visitor_pass_issued = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prefix} {self.first_name} {self.last_name} - {self.visit_date}"


# Visitor List Model
class VisitorList(models.Model):
    MEETING_REASON_CHOICES = [
        ("Software Demo", "Software Demo"),
        ("Doctor Meeting", "Doctor Meeting"),
        ("Documentation Meet", "Documentation Meet"),
        ("Equipment Demo", "Equipment Demo"),
        ("Camp Meeting", "Camp Meeting"),
    ]

    visitor_name = models.CharField(max_length=255)
    visit_date = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField(blank=True, null=True)
    from_company = models.CharField(max_length=255, blank=True, null=True)
    meeting_reason = models.CharField(max_length=50, choices=MEETING_REASON_CHOICES)

    def __str__(self):
        return f"{self.visitor_name} - {self.visit_date} - {self.meeting_reason}"


# Visitor Pass Model
class VisitorPass(models.Model):
    visitor_name = models.CharField(max_length=255)
    visitor_pass_collected = models.BooleanField(default=False)
    out_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.visitor_name} - {'Pass Collected' if self.visitor_pass_collected else 'Pending'}"
