# Generated by Django 3.2.3 on 2021-06-10 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0011_auto_20210610_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='seller_shop_details',
            name='main_img',
        ),
    ]
