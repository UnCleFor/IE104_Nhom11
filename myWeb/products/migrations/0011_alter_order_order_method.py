# Generated by Django 5.0.10 on 2024-12-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_method',
            field=models.CharField(choices=[('Thanh toán tiền mặt khi nhận hàng', 'Thanh toán tiền mặt khi nhận hàng'), ('Thanh toán bằng thẻ ATM nội địa và tài khoản ngân hàng', 'Thanh toán bằng thẻ ATM nội địa và tài khoản ngân hàng')], max_length=100),
        ),
    ]