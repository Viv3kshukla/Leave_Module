# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leavemodule', '0013_auto_20170831_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.IntegerField(),
        ),
    ]
