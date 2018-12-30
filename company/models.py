from django.db import models

# Create your models here.

<<<<<<< HEAD

class Employee(models.Model):
    e_id = models.IntegerField(unique=True, primary_key=True, serialize=False, verbose_name='ID')
    e_name = models.CharField(max_length=30, verbose_name='Name')
    e_password = models.CharField(max_length=6, verbose_name='Password')
    e_email = models.CharField(max_length=30, verbose_name='Email')
    e_phone = models.IntegerField(verbose_name='Phone')
    e_degree = models.IntegerField(verbose_name='Degree')
    e_salary = models.IntegerField(verbose_name='Salary')


class Head(models.Model):
    eHead = models.ForeignKey(Employee, unique=True, primary_key=True, serialize=False, verbose_name='Employee')
    h_degree = models.IntegerField(verbose_name='Head Degree')
=======
class Company(models.Model):
    c_id = models.IntegerField(unique=True, primary_key=True, verbose_name='ID')
    c_name =  models.CharField(max_length = 30, verbose_name='Company Name')
    c_email = models.CharField(max_length=30, verbose_name='Company E-mail')
    c_address =  models.TextField(verbose_name='Company Address')
    c_password =  models.CharField(max_length=6,  verbose_name='Company Password')

    def __str__(self):
        return self.c_name
>>>>>>> 8bf9ffe4593b75545ebabd4a4926273fe50c088e
