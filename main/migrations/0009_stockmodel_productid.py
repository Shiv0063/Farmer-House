# Generated by Django 5.0.4 on 2024-04-24 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_stockmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmodel',
            name='ProductId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
