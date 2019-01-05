from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Employee
from .forms import EmployeeForm
from .models import Department
from .forms import DepartmentForm
from .forms import Project
from .forms import ProjectForm
from django.contrib import messages
from django.utils.text import slugify


def employee_index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})


def employee_detail(request, e_slug):
    employees = get_object_or_404(Employee, e_slug=e_slug)
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


def employee_update(request, e_slug):
    employees = get_object_or_404(Employee, e_slug=e_slug)
    form = EmployeeForm(request.POST or None, instance=employees)
    if form.is_valid():
        form.save()
        messages.success(request, "Employee is updated, successfully!")
        return HttpResponseRedirect(employees.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'employee/update.html', context)


def employee_delete(request, e_slug):
    employees = get_object_or_404(Employee, e_slug=e_slug)
    employees.delete()
    return redirect('app:index')

##########################################################


def department_index(request):
    departments = Department.objects.all()
    return render(request, 'department/index.html', {'departments': departments})


def department_detail(request, d_slug):
    departments = get_object_or_404(Department, d_slug=d_slug)
    context = {
        'department': departments,
    }

    return render(request, 'department/detail.html', context)


def department_create(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        departments = form.save()
        messages.success(request, "Department is created, successfully!")
        return HttpResponseRedirect(departments.get_department_url())

    context = {
        'form': form,
    }
    return render(request, 'department/form.html', context)


def department_update(request, d_slug):
    departments = get_object_or_404(Department, d_slug=d_slug)
    form = DepartmentForm(request.POST or None, instance=departments)
    if form.is_valid():
        form.save()
        messages.success(request, "Department is updated, successfully!")
        return HttpResponseRedirect(departments.get_department_url())

    context = {
        'form': form,
    }
    return render(request, 'department/update.html', context)


def department_delete(request, d_slug):
    departments = get_object_or_404(Department, d_slug=d_slug)
    departments.delete()
    return redirect('app:indexD')

##########################################################


def project_index(request):
    projects = Project.objects.all()
    return render(request, 'project/index.html', {'projects': projects})


def project_detail(request, p_slug):
    projects = get_object_or_404(Project, p_slug=p_slug)
    context = {
        'project': projects,
    }

    return render(request, 'project/detail.html', context)


def project_create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        projects = form.save()
        messages.success(request, "Project is created, successfully!")
        return HttpResponseRedirect(projects.get_project_url())

    context = {
        'form': form,
    }
    return render(request, 'project/form.html', context)


def project_update(request, p_slug):
    projects = get_object_or_404(Project, p_slug=p_slug)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=projects)
    if form.is_valid():
        form.save()
        messages.success(request, "Project is updated, successfully!")
        return HttpResponseRedirect(projects.get_project_url())

    context = {
        'form': form,
    }
    return render(request, 'project/update.html', context)


def project_delete(request, p_slug):
    projects = get_object_or_404(Project, p_slug=p_slug)
    projects.delete()
    return redirect('app:indexP')
