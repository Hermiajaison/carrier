# Generated by Django 5.0.7 on 2024-08-08 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycarrier', '0002_rename_adminregistation_adminregistration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminregistration',
            old_name='CHOOSE',
            new_name='USERTYPE',
        ),
    ]
