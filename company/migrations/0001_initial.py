# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-10 19:09
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Company ID')),
                ('c_name', models.CharField(max_length=30, verbose_name='Company Name')),
                ('c_email', models.EmailField(max_length=254, verbose_name='Company E-mail')),
                ('c_address', ckeditor.fields.RichTextField(verbose_name='Company Address')),
                ('c_phone', models.CharField(max_length=20, verbose_name='Company Phone')),
                ('c_password', models.CharField(max_length=6, verbose_name='Company Password')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('d_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Department ID')),
                ('d_name', models.CharField(max_length=30, verbose_name='Department Name')),
                ('d_capacity', models.IntegerField(verbose_name='Department Capacity')),
                ('d_phone', models.IntegerField(verbose_name='Department Phone')),
                ('d_password', models.CharField(max_length=6, verbose_name='Department Password')),
                ('d_slug', models.SlugField(editable=False, max_length=130, unique=True)),
            ],
            options={
                'ordering': ['dCompany'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('e_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Employee ID')),
                ('e_name', models.CharField(max_length=30, verbose_name='Name')),
                ('e_surname', models.CharField(max_length=30, verbose_name='Surname')),
                ('e_password', models.CharField(max_length=6, verbose_name='Password')),
                ('e_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('e_phone', models.IntegerField(verbose_name='Phone')),
                ('e_degree', models.IntegerField(verbose_name='Degree')),
                ('e_salary', models.IntegerField(verbose_name='Salary')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='')),
                ('e_slug', models.SlugField(editable=False, max_length=130, unique=True)),
            ],
            options={
                'ordering': ['eCompany', 'eDepartment', '-e_degree'],
            },
        ),
        migrations.CreateModel(
            name='Helps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_price', models.IntegerField(verbose_name='Project Price')),
                ('h_type', models.CharField(max_length=50, verbose_name='Help Type')),
                ('h_timestart', models.DateTimeField(verbose_name='Help Time Start')),
                ('h_timeend', models.DateTimeField(verbose_name='Help Time End')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('i_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Issue ID')),
                ('i_type', models.CharField(max_length=30, verbose_name='Issue Type')),
                ('i_extra', ckeditor.fields.RichTextField(verbose_name='Issue Notes')),
                ('i_content', ckeditor.fields.RichTextField(verbose_name='Issue Content')),
                ('i_slug', models.SlugField(editable=False, max_length=130, unique=True)),
            ],
            options={
                'ordering': ['i_id'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Project ID')),
                ('p_startdate', models.DateTimeField(verbose_name='Project Start Date')),
                ('p_enddate', models.DateTimeField(verbose_name='Project End Date')),
                ('p_title', models.CharField(max_length=75, verbose_name='Project Title')),
                ('p_situation', models.CharField(max_length=20, verbose_name='Project Situation')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('p_slug', models.SlugField(editable=False, max_length=130, unique=True)),
            ],
            options={
                'ordering': ['p_enddate'],
            },
        ),
        migrations.CreateModel(
            name='ProjectPlan',
            fields=[
                ('plan_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Plan ID')),
                ('plan_type', models.CharField(max_length=30, verbose_name='Plan Type')),
                ('plan_date', models.DateTimeField(verbose_name='Plan Date')),
                ('pProjectPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Project', verbose_name='Project ID')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_type', models.CharField(max_length=30, verbose_name='Report Type')),
                ('r_version', models.CharField(max_length=5, verbose_name='Report Version')),
                ('r_createdate', models.DateTimeField(verbose_name='Report Create Date')),
                ('pReport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Project', verbose_name='Project ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('sub_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Subtask ID')),
                ('sub_content', ckeditor.fields.RichTextField(verbose_name='Subtask Content')),
                ('sub_slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('iIssue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Issue', verbose_name='Issue ID')),
            ],
            options={
                'ordering': ['sub_id'],
            },
        ),
        migrations.CreateModel(
            name='WorkFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_type', models.CharField(max_length=30, verbose_name='Workflow Type')),
                ('w_date', models.DateTimeField(verbose_name='Workflow Date')),
            ],
        ),
        migrations.CreateModel(
            name='ForeignCompany',
            fields=[
                ('company_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='company.Company')),
                ('f_rating', models.IntegerField(verbose_name='Foreign Company Rating')),
            ],
            bases=('company.company',),
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('eHead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='company.Employee', unique=True, verbose_name='Employee')),
                ('h_degree', models.IntegerField(verbose_name='Head Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('eOther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='company.Employee', unique=True, verbose_name='Employee')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='cProject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Company Name'),
        ),
        migrations.AddField(
            model_name='project',
            name='dProject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Department', verbose_name='Department Name'),
        ),
        migrations.AddField(
            model_name='project',
            name='eProject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eProject', to='company.Employee', verbose_name='Project Manager'),
        ),
        migrations.AddField(
            model_name='project',
            name='sProject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sProject', to='company.Employee'),
        ),
        migrations.AddField(
            model_name='issue',
            name='pIssue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Project', verbose_name='Project ID'),
        ),
        migrations.AddField(
            model_name='helps',
            name='cHelps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Which Company Helps (ID)'),
        ),
        migrations.AddField(
            model_name='helps',
            name='pHelps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Project', verbose_name='Which Project Helps (ID)'),
        ),
        migrations.AddField(
            model_name='employee',
            name='eCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Company Name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='eDepartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Department', verbose_name='Department Name'),
        ),
        migrations.AddField(
            model_name='department',
            name='dCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Company Name'),
        ),
        migrations.AddField(
            model_name='report',
            name='oReport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Other', verbose_name='Prepare Employee ID'),
        ),
        migrations.AddField(
            model_name='projectplan',
            name='headMakes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Head', verbose_name='Head ID'),
        ),
        migrations.AddField(
            model_name='other',
            name='o_studyproject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Project', verbose_name='Works Project ID'),
        ),
        migrations.AddField(
            model_name='issue',
            name='i_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Other', verbose_name='Assign Employee'),
        ),
        migrations.AddField(
            model_name='head',
            name='pManage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Project', verbose_name='Manages Project ID'),
        ),
    ]
