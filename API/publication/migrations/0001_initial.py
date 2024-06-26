# Generated by Django 5.0.6 on 2024-06-01 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField()),
                ('edition', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('published', 'Published'), ('out_of_circulation', 'Out of Circulation'), ('in_printing', 'In Printing'), ('in_test_layout', 'In Test Layout'), ('in_test_ink', 'In Test Ink'), ('in_review', 'In Review'), ('all_sold', 'All Sold'), ('pre_sale', 'Pre-Sale')], max_length=20)),
                ('quantity', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='books.book')),
            ],
        ),
    ]
