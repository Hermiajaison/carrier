# Generated by Django 5.0.7 on 2024-08-22 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarrier', '0021_user_jobseeker_jobseeker_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_jobseeker',
            name='jobseeker_location',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
