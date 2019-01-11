# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-11 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30, verbose_name='Name')),
                ('customer_stage', models.IntegerField(verbose_name='Stage')),
                ('customer_phone', models.IntegerField(verbose_name='Phone')),
            ],
        ),
    ]
