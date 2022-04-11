from rest_framework import serializers

from .models import EmployeeData

class EmployeeSerializer(serializers.MoldeSerializer):
    class Meta:
        model = EmployeeData
        fields = ['id','emp_no','first_name','last_name','gender','birth_date','address','hire_date']