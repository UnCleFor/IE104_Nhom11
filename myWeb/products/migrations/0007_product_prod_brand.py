# Generated by Django 5.0.10 on 2024-12-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_image_prod_cate_lv1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_brand',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
