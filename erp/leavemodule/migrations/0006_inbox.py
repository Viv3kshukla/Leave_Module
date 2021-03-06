# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_departmenthead'),
        ('leavemodule', '0005_application_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('pf_reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pf_reciever', to='basic.User')),
                ('pf_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pf_sender', to='basic.User')),
            ],
        ),
    ]
