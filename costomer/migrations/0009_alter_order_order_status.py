# Generated by Django 3.2.3 on 2021-06-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costomer', '0008_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
