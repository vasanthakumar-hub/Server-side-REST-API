from rest_framework import serializers
from . models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Employees
        fields = ('EmployeeID','EmployeeName','Department','DateOfJoining','PhotoFileName')