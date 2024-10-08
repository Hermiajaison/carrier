# Generated by Django 5.0.7 on 2024-08-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarrier', '0005_delete_adminregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='employer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMPLOYER_NAME', models.CharField(max_length=100)),
                ('COMPANY_NAME', models.CharField(max_length=100)),
                ('EMPLOYER_EMAIL', models.CharField(max_length=100)),
                ('EMPLOYER_LOCATION', models.CharField(max_length=100)),
                ('EMPLOYER_STATE', models.CharField(max_length=100)),
                ('EMPLOYER_PROFESSION', models.CharField(max_length=100)),
                ('EMPLOYER_AGE', models.CharField(max_length=100)),
                ('EMPLOYER_JOB_NATURE', models.CharField(max_length=100)),
                ('EMPLOYER_PHONE', models.CharField(max_length=100)),
                ('EMPLOYER_IMAGE', models.ImageField(upload_to='profile_pfp')),
                ('COMPANY_LOGO', models.ImageField(upload_to='profile_pfp')),
            ],
        ),
    ]
