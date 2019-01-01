from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

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
        form.save()

    context = {
        'form': form,
    }
    return render(request, 'employee/form.html', context)
