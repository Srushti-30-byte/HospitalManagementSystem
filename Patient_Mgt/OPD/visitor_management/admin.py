from django.contrib import admin
from .models import VisitorDetails, VisitorList, VisitorPass

# Register your models here.
admin.site.register(VisitorDetails)
admin.site.register(VisitorList)
admin.site.register(VisitorPass)
