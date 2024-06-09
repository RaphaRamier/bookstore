# Generated by Django 5.0.6 on 2024-06-08 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components', '0002_component_date'),
        ('sales', '0003_sale_sale_number'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashInFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inflow', to='sales.sale')),
            ],
        ),
        migrations.CreateModel(
            name='CashOutFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SERVICE', 'Service'), ('MATERIAL', 'Material')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='material', to='components.component')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outflow', to='suppliers.supplier')),
            ],
        ),
    ]
