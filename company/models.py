from django.db import models

# Create your models here.

class Company(models.Model):
    c_id = models.IntegerField(unique=True, primary_key=True)
    c_name =  models.CharField(max_length = 120, verbose_name='Company Name')
    c_email = models.CharField(verbose_name='Company E-mail')
    c_address =  models.TextField(verbose_name='Company Address')
    c_password =  models.CharField(max_length=10,  verbose_name='Company Password')

    def __str__(self):
        return self.c_name
