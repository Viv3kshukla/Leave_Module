# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0012_remove_departmenthead_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmenthead',
            name='temp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp', to='basic.User'),
        ),
    ]
