# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0003_action_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='featured_only',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
