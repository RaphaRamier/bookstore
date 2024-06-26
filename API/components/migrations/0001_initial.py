# Generated by Django 5.0.6 on 2024-06-03 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='suppliers.supplier')),
            ],
        ),
    ]
