# Generated by Django 3.2.9 on 2021-11-07 03:29

import convite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='convite',
            name='codigo',
            field=models.CharField(blank=True, default=convite.models.create_if_hash, max_length=10, null=True, unique=True),
        ),
    ]
