# Generated by Django 5.0 on 2024-02-26 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
