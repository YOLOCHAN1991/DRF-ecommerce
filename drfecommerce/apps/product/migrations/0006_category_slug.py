# Generated by Django 4.2.5 on 2023-09-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0005_alter_productline_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default="ee", max_length=100),
            preserve_default=False,
        ),
    ]
