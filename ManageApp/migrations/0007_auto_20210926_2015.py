# Generated by Django 3.1.7 on 2021-09-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageApp', '0006_location_product_productmovement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmovement',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
