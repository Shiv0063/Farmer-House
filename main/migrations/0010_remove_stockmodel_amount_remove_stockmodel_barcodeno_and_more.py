# Generated by Django 5.0.4 on 2024-04-24 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_stockmodel_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockmodel',
            name='Amount',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='BarcodeNo',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='MRP',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='MaxQty',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='MinQty',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='ProductName',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='PurchasePrice',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='SubCategory',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='Tax',
        ),
        migrations.RemoveField(
            model_name='stockmodel',
            name='Unit',
        ),
    ]
