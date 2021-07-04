# Generated by Django 3.2 on 2021-07-04 05:23

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20210622_1640'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='documentembedding',
            index=django.contrib.postgres.indexes.GistIndex(fields=['embedding'], name='documents_d_embeddi_c3d485_gist'),
        ),
        migrations.AddIndex(
            model_name='sentenceembedding',
            index=django.contrib.postgres.indexes.GistIndex(fields=['embedding'], name='documents_s_embeddi_7751f8_gist'),
        ),
    ]
