# Generated by Django 3.2.3 on 2021-07-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0014_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_shop_details',
            name='full_name',
            field=models.CharField(max_length=15),
        ),
    ]
