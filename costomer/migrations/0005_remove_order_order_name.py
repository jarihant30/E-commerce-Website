# Generated by Django 3.2.3 on 2021-06-08 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costomer', '0004_auto_20210609_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_name',
        ),
    ]
