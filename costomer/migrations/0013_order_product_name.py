# Generated by Django 3.2.3 on 2021-07-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costomer', '0012_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]