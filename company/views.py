from django.shortcuts import render, HttpResponse, get_list_or_404
from .models import Employee

# Create your views here.


def employee_index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})