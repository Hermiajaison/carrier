# Generated by Django 5.0.7 on 2024-08-19 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarrier', '0009_delete_employer_details_user_employer_company_logo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMPLOYER_post_a_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JOB_TITLE', models.CharField(max_length=100)),
                ('JOB_POSITION', models.CharField(max_length=100)),
                ('JOB_DESCRIPTION', models.CharField(max_length=200)),
                ('JOB_STATE', models.CharField(max_length=100)),
                ('JOB_COUNTRY', models.CharField(max_length=100)),
                ('JOB_LOCATION', models.CharField(max_length=100)),
                ('JOB_POSTED_DATE', models.CharField(max_length=100)),
                ('JOB_APPLICATION_END_DATE', models.CharField(max_length=100)),
                ('JOB_NATURE', models.CharField(max_length=100)),
                ('JOB_EDUCATION_EXPERIENCE', models.CharField(max_length=100)),
                ('JOB_REQUIRED_KNOWLEDGE', models.CharField(max_length=100)),
                ('JOB_NUMBER_OF_VACANCY', models.CharField(max_length=100)),
                ('JOB_SALARY', models.CharField(max_length=100)),
                ('JOB_WEBSITE', models.CharField(max_length=100)),
                ('DETAILS_OF_COMPANY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycarrier.user_employer')),
            ],
        ),
    ]
