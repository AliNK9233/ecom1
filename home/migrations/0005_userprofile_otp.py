# Generated by Django 5.0 on 2024-01-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_userprofile_otp1'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
