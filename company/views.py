from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Employee
from .forms import EmployeeForm
from .models import Department
from .forms import DepartmentForm
from django.contrib import messages

def employee_index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})

def employee_detail(request, id):
    employees = get_object_or_404(Employee, e_id=id)
    context = {
        'employee': employees,
    }

    return render(request, 'employee/detail.html', context)

def employee_create(request):

    # if request.method == "POST":
    #     Formdan gelen bilgileri kaydet
    #    form = EmployeeForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    # else:
    #    formu kullanıcıya göster
    #    form = EmployeeForm()

    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        employees = form.save()
        messages.success(request, "Employee is created, successfully!")
        return HttpResponseRedirect(employees.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'employee/form.html', context)

def employee_update(request, id):
    employees = get_object_or_404(Employee, e_id=id)
    form = EmployeeForm(request.POST or None, instance=employees)
    if form.is_valid():
        form.save()
        messages.success(request, "Employee is updated, successfully!")
        return HttpResponseRedirect(employees.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'employee/update.html', context)

def employee_delete(request, id):
    employees = get_object_or_404(Employee, e_id=id)
    employees.delete()
    return redirect('employee:index')

##########################################################
def department_index(request):
    departments = Department.objects.all()
    return render(request, 'department/index.html', {'departments': departments})

def department_detail(request, id):
    departments = get_object_or_404(Department, d_id=id)
    context = {
        'department': departments,
    }

    return render(request, 'department/detail.html', context)

def department_create(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        departments = form.save()
        messages.success(request, "Department is created, successfully!")
        return HttpResponseRedirect(departments.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'department/form.html', context)


def department_update(request, id):
    departments = get_object_or_404(Department, d_id=id)
    form = DepartmentForm(request.POST or None, instance=departments)
    if form.is_valid():
        form.save()
        messages.success(request, "Department is updated, successfully!")
        return HttpResponseRedirect(departments.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'department/update.html', context)

def department_delete(request, id):
    departments = get_object_or_404(Department, d_id=id)
    departments.delete()
    return redirect('department:index')
