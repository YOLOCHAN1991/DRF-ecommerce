# Generated by Django 4.2.5 on 2023-09-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_productline_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productline",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
