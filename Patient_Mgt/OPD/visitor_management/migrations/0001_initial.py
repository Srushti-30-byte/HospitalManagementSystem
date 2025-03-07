# Generated by Django 5.1.5 on 2025-03-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_type', models.CharField(choices=[('new', 'New Visitor'), ('existing', 'Existing Visitor')], default='new', max_length=10)),
                ('visit_date', models.DateField()),
                ('in_time', models.TimeField()),
                ('prefix', models.CharField(choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Dr', 'Dr')], max_length=10)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('mobile_no', models.CharField(max_length=15)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('visitor_card', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='visitor_photos/')),
                ('doctor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('appointment_taken', models.BooleanField(default=False)),
                ('meeting_reason', models.CharField(choices=[('Software Demo', 'Software Demo'), ('Doctor Meeting', 'Doctor Meeting'), ('Documentation Meet', 'Documentation Meet'), ('Equipment Demo', 'Equipment Demo'), ('Camp Meeting', 'Camp Meeting')], default='Doctor Meeting', max_length=40)),
                ('visitor_blacklisted', models.BooleanField(default=False)),
                ('is_vip', models.BooleanField(default=False)),
                ('visitor_pass_issued', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=255)),
                ('visit_date', models.DateField()),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField(blank=True, null=True)),
                ('from_company', models.CharField(blank=True, max_length=255, null=True)),
                ('meeting_reason', models.CharField(choices=[('Software Demo', 'Software Demo'), ('Doctor Meeting', 'Doctor Meeting'), ('Documentation Meet', 'Documentation Meet'), ('Equipment Demo', 'Equipment Demo'), ('Camp Meeting', 'Camp Meeting')], max_length=50)),
            ],
        ),
    ]
