# Generated by Django 5.0.3 on 2024-11-19 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_pyrlclient'),
        ('products', '0005_rename_product_category_productcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='company_id',
        ),
        migrations.AddField(
            model_name='product',
            name='client_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='base.pyrlclient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='client_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.pyrlclient'),
            preserve_default=False,
        ),
    ]
