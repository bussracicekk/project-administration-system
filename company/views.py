from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Employee
from .forms import EmployeeForm
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
