from django.contrib import admin
from .models import EmployeeData

# Register your models here.
@admin.register(EmployeeData)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_no']