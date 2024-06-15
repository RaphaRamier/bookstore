# Generated by Django 5.0.6 on 2024-06-05 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0002_remove_bookassembly_page_count'),
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='assembly',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assembly', to='assembly.bookassembly'),
        ),
        migrations.AddField(
            model_name='publication',
            name='language',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='page_count',
            field=models.IntegerField(default=0),
        ),
    ]