# Generated by Django 5.0.6 on 2024-06-10 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0003_alter_cashinflow_source'),
        ('sales', '0005_alter_sale_book_alter_sale_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashinflow',
            name='source',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='inflow', to='sales.sale'),
        ),
    ]
