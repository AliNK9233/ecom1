# Generated by Django 5.0 on 2024-01-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_variant_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='image',
            field=models.ImageField(null=True, upload_to='varient_images'),
        ),
    ]
