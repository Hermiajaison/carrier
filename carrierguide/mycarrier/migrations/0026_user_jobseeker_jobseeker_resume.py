# Generated by Django 5.0.7 on 2024-08-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarrier', '0025_user_jobseeker_jobseeker_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_jobseeker',
            name='jobseeker_resume',
            field=models.FileField(blank=True, null=True, upload_to='profile_pfp'),
        ),
    ]
