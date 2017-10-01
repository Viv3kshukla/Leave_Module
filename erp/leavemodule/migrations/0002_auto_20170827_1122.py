# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leavemodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sanction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
                ('sanction_cl_rh', models.CharField(max_length=50)),
                ('sanction_others', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='application',
            name='acad_pf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acad_pf', to='basic.User'),
        ),
        migrations.AlterField(
            model_name='application',
            name='admin_pf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adin_pf', to='basic.User'),
        ),
    ]
