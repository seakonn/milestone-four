# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-24 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0006_commission_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
