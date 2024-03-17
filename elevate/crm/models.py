from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=150, default='null')
    last_name = models.CharField(max_length=150, default='null')
    ifsc_code = models.CharField(max_length=100, default='null')
    bank_account = models.CharField(max_length=1000, default='null')
    date_of_joining = models.CharField(max_length=100, default='null')
    date_of_birth = models.CharField(max_length=100, default='null')
    status = models.CharField(max_length=100, default='null')
    gender = models.CharField(max_length=100, default='null')
    