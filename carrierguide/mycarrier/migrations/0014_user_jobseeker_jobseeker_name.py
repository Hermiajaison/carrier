# Generated by Django 5.0.7 on 2024-08-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycarrier', '0013_alter_employer_post_a_job_job_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_jobseeker',
            name='jobseeker_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
