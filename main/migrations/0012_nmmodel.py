# Generated by Django 5.0.4 on 2024-04-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_stockmodel_amount_stockmodel_barcodeno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NMModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductId', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
