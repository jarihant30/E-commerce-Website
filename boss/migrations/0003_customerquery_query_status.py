# Generated by Django 3.2.3 on 2021-06-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boss', '0002_customerquery'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerquery',
            name='query_status',
            field=models.IntegerField(default=1),
        ),
    ]
