# Generated by Django 5.0.7 on 2024-11-12 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
        ("user_management", "0002_remove_pyrluser_address_line_1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pyrluser",
            name="company",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.company",
            ),
        ),
    ]
