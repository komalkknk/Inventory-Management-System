# Generated by Django 3.1.7 on 2021-09-28 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageApp', '0013_remove_productmovement_warehouse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmovement',
            name='from_location',
        ),
        migrations.RemoveField(
            model_name='productmovement',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='productmovement',
            name='to_location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductMovement',
        ),
    ]
