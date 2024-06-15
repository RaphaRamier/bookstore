# Generated by Django 5.0.6 on 2024-06-10 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0004_alter_publication_quantity'),
        ('sales', '0004_sale_description_alter_sale_book_alter_sale_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='publication.publication'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='description',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='sale',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]