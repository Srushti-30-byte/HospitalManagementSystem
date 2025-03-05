from django.db import models
from django.db import models


class CompanySettlement(models.Model):
    date = models.DateTimeField(auto_now_add=True)  # Auto store current date/time
    company_name = models.CharField(max_length=255)

    from_date = models.DateField()
    to_date = models.DateField()

    patient_name = models.CharField(max_length=255, blank=True, null=True)
    uhid = models.CharField(max_length=50, blank=True, null=True)  # Unique Health ID
    op_ip_no = models.CharField(max_length=50, blank=True, null=True)  # OP/IP Number

    bill_no = models.CharField(max_length=50, unique=True)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    approved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tds_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    wrf_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_net_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def __str__(self):
        return f"Bill No: {self.bill_no} - {self.company_name}"
