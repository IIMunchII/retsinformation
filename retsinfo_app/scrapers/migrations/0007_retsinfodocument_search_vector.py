# Generated by Django 3.2 on 2021-05-13 15:15

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0006_auto_20210510_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='retsinfodocument',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(default=''),
            preserve_default=False,
        ),
    ]
