# Generated by Django 5.0.4 on 2024-04-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_productmodel_categorymodel_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='Category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='SubCategory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]