# Generated by Django 5.0.7 on 2024-09-11 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarrier', '0033_alter_jobseeker_apply_job_details_of_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker_apply_job',
            name='DETAILS_OF_EMPLOYER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycarrier.user_jobseeker'),
        ),
    ]
