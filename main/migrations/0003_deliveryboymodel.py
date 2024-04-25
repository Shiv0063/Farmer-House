# Generated by Django 5.0.4 on 2024-04-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_categorymodel_subcategorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryBoyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Number', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.TextField()),
                ('Licence', models.FileField(blank=True, null=True, upload_to='DeliveryBoy')),
                ('AdharCard', models.FileField(blank=True, null=True, upload_to='DeliveryBoy')),
                ('PanCard', models.FileField(blank=True, null=True, upload_to='DeliveryBoy')),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('PassWord', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]