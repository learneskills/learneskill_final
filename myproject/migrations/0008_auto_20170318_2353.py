# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-18 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0007_auto_20170225_0027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-title']},
        ),
    ]
