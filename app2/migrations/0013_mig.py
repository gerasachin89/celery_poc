# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-12 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0012_remove_person_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mig_name', models.CharField(default=b'detail', max_length=30)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.Person')),
            ],
        ),
    ]
