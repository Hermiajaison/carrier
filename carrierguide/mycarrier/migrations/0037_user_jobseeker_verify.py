# Generated by Django 5.0.6 on 2024-09-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarrier', '0036_user_employer_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_jobseeker',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]
