# Generated by Django 3.2.3 on 2021-06-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costomer', '0011_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(default=0),
        ),
    ]
