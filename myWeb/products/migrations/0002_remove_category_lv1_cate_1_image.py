# Generated by Django 5.0.10 on 2024-12-10 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_lv1',
            name='cate_1_image',
        ),
    ]
