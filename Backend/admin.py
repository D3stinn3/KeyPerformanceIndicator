from django.contrib import admin
from .models import User, Employee, Department, KPI

# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(KPI)