# Generated by Django 5.0.10 on 2024-12-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_prod_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_country',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_effect',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_how_to_use',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_ingredient',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_preserve',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_side_effect',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_who_to_use',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
