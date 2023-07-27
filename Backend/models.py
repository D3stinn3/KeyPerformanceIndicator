from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(default=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.name
    
class Department(models.Model):
    department_name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.department_name
    
class Employee(models.Model):
    employee_name = models.CharField(max_length=100, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.employee_name
    
class KPI(models.Model):
    employee_kpi_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    kpi_name = models.CharField(max_length=100, null=True)
    value = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.kpi_name     
