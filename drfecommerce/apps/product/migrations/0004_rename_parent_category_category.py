# Generated by Django 4.2.5 on 2023-09-18 21:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_rename_parent_product_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="parent",
            new_name="category",
        ),
    ]
