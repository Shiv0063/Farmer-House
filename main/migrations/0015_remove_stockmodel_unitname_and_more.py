# Generated by Django 5.0.4 on 2024-04-24 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_stockmodel_unitname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockmodel',
            name='Unitname',
        ),
        migrations.AlterField(
            model_name='purchaseentrymodel',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 20, 13, 45, 70961)),
        ),
    ]