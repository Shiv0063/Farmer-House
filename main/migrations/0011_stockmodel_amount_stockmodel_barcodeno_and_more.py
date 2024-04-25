# Generated by Django 5.0.4 on 2024-04-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_stockmodel_amount_remove_stockmodel_barcodeno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmodel',
            name='Amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='BarcodeNo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='Category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='MRP',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='MaxQty',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='MinQty',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='ProductName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='PurchasePrice',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='Quantity',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='SubCategory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='Tax',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockmodel',
            name='Unit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]