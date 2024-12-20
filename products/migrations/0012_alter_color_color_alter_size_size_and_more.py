# Generated by Django 5.1.3 on 2024-12-14 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='volume',
            name='volume',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='ProductVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(blank=True, max_length=50, null=True)),
                ('has_color', models.BooleanField(default=False)),
                ('colors', models.CharField(blank=True, max_length=30, null=True)),
                ('has_size', models.BooleanField(default=False)),
                ('sizes', models.CharField(blank=True, max_length=30, null=True)),
                ('has_volume', models.BooleanField(default=False)),
                ('volumes', models.CharField(blank=True, max_length=30, null=True)),
                ('stock', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=10)),
                ('discount', models.BooleanField(default=False)),
                ('off_price', models.CharField(blank=True, max_length=10, null=True)),
                ('discount_percent', models.CharField(blank=True, max_length=2, null=True)),
                ('weight', models.CharField(max_length=50)),
                ('max_order', models.CharField(max_length=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variety', to='products.product')),
            ],
        ),
    ]
