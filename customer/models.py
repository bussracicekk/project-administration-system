from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.IntegerField(unique=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_name = models.CharField(max_length=30, verbose_name='Name')
    customer_stage = models.IntegerField(verbose_name='Stage')
    customer_phone = models.IntegerField(verbose_name='Phone')
