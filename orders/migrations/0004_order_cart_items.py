# Generated by Django 5.0 on 2024-01-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_rename_description_usercart_title'),
        ('orders', '0003_alter_order_delivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_items',
            field=models.ManyToManyField(related_name='order_cart_items', to='cart.usercart'),
        ),
    ]
