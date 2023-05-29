from django.shortcuts import render,redirect
from .models import Employee



# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'attendance/employee_list.html', {'employees': employees})

