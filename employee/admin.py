from django.contrib import admin
from .models import EmployeeData

# Register your models here.
@admin.register(EmployeeData)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name', 'hire_date')
