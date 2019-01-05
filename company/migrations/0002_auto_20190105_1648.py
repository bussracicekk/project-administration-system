# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-05 13:48
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='c_address',
            field=ckeditor.fields.RichTextField(verbose_name='Company Address'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='i_content',
            field=ckeditor.fields.RichTextField(verbose_name='Issue Content'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='i_extra',
            field=ckeditor.fields.RichTextField(verbose_name='Issue Notes'),
        ),
    ]
