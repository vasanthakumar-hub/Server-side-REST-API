from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments,Employees
from .serializers import DepartmentSerializer,EmployeeSerializer

# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added record Successfully", safe=False)
        return JsonResponse("Failed to Add a record", safe=False)
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Record Successfully", safe=False)
        return JsonResponse("Failed to Update the Record", safe=False)
    elif request.method=='DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return  JsonResponse("Record Deleted Successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
