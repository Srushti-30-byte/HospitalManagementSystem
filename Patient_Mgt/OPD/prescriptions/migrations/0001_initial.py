# Generated by Django 5.1.5 on 2025-03-05 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('uhid', models.CharField(blank=True, max_length=50, null=True)),
                ('prescription_date', models.DateField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('drug_name', models.CharField(blank=True, max_length=255, null=True)),
                ('doctor_name', models.CharField(max_length=255)),
                ('remark', models.TextField(blank=True, null=True)),
                ('total_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
