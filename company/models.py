from django.db import models

# Create your models here.

class Company(models.Model):
    c_id = models.IntegerField(unique=True, primary_key=True)
    c_name =  models.CharField(max_length = 120)
    c_email = models.TextField()
    c_address =  models.TextField()
    c_password =  models.TextField(max_length=10)