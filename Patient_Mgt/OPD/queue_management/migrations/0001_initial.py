# Generated by Django 5.1.5 on 2025-03-03 08:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueueManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient_name', models.CharField(max_length=255)),
                ('cabin_number', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(choices=[('General Medicine', 'General Medicine'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Orthopedics', 'Orthopedics'), ('Pediatrics', 'Pediatrics'), ('Gynecology', 'Gynecology'), ('Dermatology', 'Dermatology'), ('ENT', 'ENT'), ('Ophthalmology', 'Ophthalmology'), ('Psychiatry', 'Psychiatry'), ('Urology', 'Urology'), ('Oncology', 'Oncology'), ('Radiology', 'Radiology'), ('Pulmonology', 'Pulmonology'), ('Nephrology', 'Nephrology')], max_length=100)),
                ('doctor_name', models.CharField(max_length=255)),
                ('ref_doctor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('appointment_type', models.CharField(choices=[('Phone Appointment', 'Phone Appointment'), ('Walk-in Patient', 'Walk-in Patient'), ('Mobile App Appointment', 'Mobile App Appointment')], max_length=50)),
                ('is_called', models.BooleanField(default=False)),
            ],
        ),
    ]
