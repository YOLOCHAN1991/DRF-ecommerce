# Generated by Django 4.2.5 on 2023-09-23 07:57

import apps.product.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_brand_is_active_category_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="productline",
            name="order",
            field=apps.product.fields.OrderField(blank=True, default=1),
            preserve_default=False,
        ),
    ]