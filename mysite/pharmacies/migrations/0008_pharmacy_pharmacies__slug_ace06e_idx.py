# Generated by Django 4.2.20 on 2025-03-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pharmacies", "0007_product_form"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="pharmacy",
            index=models.Index(fields=["slug"], name="pharmacies__slug_ace06e_idx"),
        ),
    ]
