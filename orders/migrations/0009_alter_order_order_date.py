# Generated by Django 5.0 on 2024-01-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_delete_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
