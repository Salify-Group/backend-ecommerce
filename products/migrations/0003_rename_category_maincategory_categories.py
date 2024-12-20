# Generated by Django 5.1.3 on 2024-12-12 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='MainCategory',
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.ManyToManyField(blank=True, null=True, to='products.maincategory')),
                ('sub_category', models.ForeignKey(default='دسنه بندی نشده', on_delete=django.db.models.deletion.SET_DEFAULT, to='products.subcategory')),
            ],
        ),
    ]
