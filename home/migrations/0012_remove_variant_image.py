# Generated by Django 5.0 on 2024-01-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_productimage_product_productimage_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='image',
        ),
    ]
