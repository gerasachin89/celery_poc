# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-12 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0011_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='detail',
        ),
    ]