# Generated by Django 4.2.5 on 2023-09-18 20:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="category",
            new_name="parent",
        ),
    ]
