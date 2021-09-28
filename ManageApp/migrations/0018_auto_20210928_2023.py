# Generated by Django 3.1.7 on 2021-09-28 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ManageApp', '0017_auto_20210928_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMovement',
            fields=[
                ('movement_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('from_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_location', to='ManageApp.location')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_id', to='ManageApp.product')),
                ('to_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_location', to='ManageApp.location')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pm_warehouse', to='ManageApp.warehousename')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_warehouse', to='ManageApp.warehousename'),
        ),
    ]
