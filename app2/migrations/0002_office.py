# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(max_length=30)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.Person')),
            ],
        ),
    ]
