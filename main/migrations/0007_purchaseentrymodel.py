# Generated by Django 5.0.4 on 2024-04-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseEntryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('TypeofPurchase', models.CharField(max_length=100)),
                ('BillNo', models.CharField(max_length=100)),
                ('InvoiceNo', models.CharField(max_length=100)),
                ('DateTime', models.DateTimeField()),
                ('TypeofPayment', models.CharField(max_length=100)),
                ('PartyName', models.CharField(max_length=100)),
                ('ProductId', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('Amount', models.CharField(max_length=100)),
            ],
        ),
    ]
