# Generated by Django 5.1.3 on 2024-12-12 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_cart'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('cart_customer', 'cart_product')},
        ),
    ]
