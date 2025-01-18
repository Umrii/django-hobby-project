# Generated by Django 5.1.5 on 2025-01-18 18:53

import localflavor.pk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.pk.models.PKStateField(default='None', max_length=5),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_1',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
