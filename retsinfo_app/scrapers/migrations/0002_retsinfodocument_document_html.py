# Generated by Django 3.2 on 2021-05-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='retsinfodocument',
            name='document_html',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
