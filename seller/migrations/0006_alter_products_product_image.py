# Generated by Django 3.2.3 on 2021-06-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_alter_seller_shop_details_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(upload_to='product/image'),
        ),
    ]
