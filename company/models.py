from django.db import models
# Create your models here.

class Company(models.Model):
    c_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Company ID')
    c_name = models.CharField(max_length=30, verbose_name='Company Name')
    c_email = models.CharField(max_length=30, verbose_name='Company E-mail')
    c_address = models.TextField(verbose_name='Company Address')
    c_phone = models.CharField(max_length = 20, verbose_name = 'Company Phone')
    c_password = models.CharField(max_length=6,  verbose_name='Company Password')

class Department(models.Model):
    d_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Department ID')
    d_name = models.CharField(max_length=30, verbose_name='Department Name')
    d_capacity = models.IntegerField(verbose_name='Department Capacity')
    d_password = models.CharField(max_length=6, verbose_name='Department Password')
    dCompany = models.ForeignKey(Company,verbose_name='Company id' )

class Project(models.Model):
    p_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Project ID')
    p_startdate = models.DateTimeField(verbose_name='Project Start Date Name')
    p_enddate = models.DateTimeField(verbose_name='Project End Date Name')
    p_title = models.CharField(max_length = 75, verbose_name = 'Project Title')
    p_situation = models.CharField(max_length = 20 , verbose_name= 'Project Situation')
    dProject = models.ForeignKey(Department, verbose_name = 'Deparment ID')

class Issue(models.Model):
    i_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Issue ID')
    i_type= models.CharField(max_length=30, verbose_name='Issue Type')
    i_extra = models.TextField(verbose_name='Issue Notes')
    i_content = models.TextField(verbose_name = 'Issue Content')
    pIssue = models.ForeignKey(Project, verbose_name = 'Project ID')

class Subtask(models.Model):
    sub_id = models.IntegerField(unique=True, primary_key=True, verbose_name='Subtask ID')
    iIssue = models.ForeignKey(Issue, verbose_name = 'Issue ID')

class Employee(models.Model):
    e_id = models.IntegerField(unique=True, primary_key=True, serialize=False, verbose_name='Employee ID')
    e_name = models.CharField(max_length=30, verbose_name='Name')
    e_password = models.CharField(max_length=6, verbose_name='Password')
    e_email = models.CharField(max_length=30, verbose_name='Email')
    e_phone = models.IntegerField(verbose_name='Phone')
    e_degree = models.IntegerField(verbose_name='Degree')
    e_salary = models.IntegerField(verbose_name='Salary')

class Other(models.Model):
    o_studyproject = models.ForeignKey(Project,verbose_name = 'Works Project ID')
    eOther = models.ForeignKey(Employee, unique=True, primary_key=True, serialize=False, verbose_name='Employee')

class Head(models.Model):
    eHead = models.ForeignKey(Employee, unique=True, primary_key=True, serialize=False, verbose_name='Employee')
    h_degree = models.IntegerField(verbose_name='Head Degree')