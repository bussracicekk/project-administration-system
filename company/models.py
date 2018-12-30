from django.db import models
# Create your models here.


class Company(models.Model):
    c_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Company ID')
    c_name = models.CharField(max_length=30, verbose_name='Company Name')
    c_email = models.CharField(max_length=30, verbose_name='Company E-mail')
    c_address = models.TextField(verbose_name='Company Address')
    c_password = models.CharField(max_length=6,  verbose_name='Company Password')


class Department(models.Model):
    d_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Department ID')
    d_name = models.CharField(max_length=30, verbose_name='Department Name')
    d_capacity = models.IntegerField(verbose_name='Department Capacity')
    d_password = models.CharField(max_length=6, verbose_name='Department Password')


class Employee(models.Model):
    e_id = models.IntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Employee ID')
    e_name = models.CharField(max_length=30, verbose_name='Name')
    e_password = models.CharField(max_length=6, verbose_name='Password')
    e_email = models.CharField(max_length=30, verbose_name='Email')
    e_phone = models.IntegerField(verbose_name='Phone')
    e_degree = models.IntegerField(verbose_name='Degree')
    e_salary = models.IntegerField(verbose_name='Salary')


class Head(models.Model):
    eHead = models.ForeignKey(Employee, unique=True, primary_key=True, serialize=False, verbose_name='Employee')
    h_degree = models.IntegerField(verbose_name='Head Degree')