# Generated by Django 3.2.3 on 2021-07-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costomer', '0013_order_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_price',
        ),
        migrations.AddField(
            model_name='order',
            name='product_description',
            field=models.TextField(default=''),
        ),
    ]