# Generated by Django 5.1.6 on 2025-03-02 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('pharmacy_number', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('opening_hours', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Pharmacy',
                'verbose_name_plural': 'Pharmacies',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('serial', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expiry_date', models.DateField()),
                ('category', models.CharField(max_length=255)),
                ('import_date', models.DateField()),
                ('internal_code', models.CharField(max_length=255)),
                ('wholesale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('distributor', models.CharField(max_length=255)),
                ('internal_id', models.CharField(max_length=255)),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='pharmacies.pharmacy')),
            ],
        ),
    ]
