# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_auto_20170829_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('Finance and Accounts', 'Finance and Accounts'), ('Establishment', 'Establishment'), ('Academics', 'Academics'), ('Computer Center', 'Computer Center'), ('ECE', 'ECE'), ('CSE', 'CSE'), ('ME', 'ME'), ('Design', 'Design'), ('Mechatronics', 'Mechatronics'), ('Natural Science', 'Natural Science'), ('Placement Cell', 'Placement Cell'), ('IWD', 'IWD'), ('Office of The Dean R&D', 'Office of The Dean R&D'), ('Directorate', 'Directorate'), ('Library', 'Library'), ('Office of The Dean P&D', 'Office of The Dean P&D'), ('Student Affairs', 'Student Affairs'), ('General Administration', 'General Administration'), ('Registrar Office', 'Registrar Office'), ('Purchase and Store', 'Purchase and Store'), ('Workshop', 'Workshop'), ('Establishment & P&S', 'Establishment & P&S'), ('F&A & GA', 'F&A & GA'), ('Security and Central Mess', 'Security and Central Mess'), ('Establishment, RTI and Rajbhasha', 'Establishment, RTI and Rajbhasha'), ('Registrar Office', 'Registrar Office')], max_length=50),
        ),
    ]
