from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Employee
from .forms import EmployeeForm
from .models import Department
from .forms import DepartmentForm
from .forms import Project
from .forms import ProjectForm
from .forms import Issue
from .forms import IssueForm
from .forms import Subtask
from .forms import SubtaskForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db import transaction, IntegrityError
from django.utils.text import slugify

######################################################################
def employee_index(request):
    employees_list = Employee.objects.all()
    query = request.GET.get('q')
    if query:
        employees_list = employees_list.filter(
            Q(e_name__icontains=query) |
            Q(e_surname__icontains=query) |
            Q(eDepartment__icontains=query)
            ).distinct()
    paginator = Paginator(employees_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        employees = paginator.page(paginator.num_pages)
    return render(request, 'employee/index.html', {'employees': employees})


def employee_detail(request, e_slug):
    employees = get_object_or_404(Employee, e_slug=e_slug)
    context = {
        'employee': employees,
    }

    return render(request, 'employee/detail.html', context)

@transaction.atomic
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
        try:
            with transaction.atomic():
                employees = form.save(commit=True)
                messages.success(request, "Employee is created, successfully!")
                return HttpResponseRedirect(employees.get_absolute_url())
        except IntegrityError:
            messages.ValidationError(request, "Employee is not created!")
    context = {
        'form': form,
    }
    return render(request, 'employee/form.html', context)

@transaction.non_atomic_requests
def employee_update(request, e_slug):
    employees = get_object_or_404(Employee, e_slug=e_slug)
    form = EmployeeForm(request.POST or None, instance=employees)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, "Employee is updated, successfully!")
        return HttpResponseRedirect(employees.get_update_url())
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
    departments_list = Department.objects.all()
    query = request.GET.get('q')
    if query:
        departments_list = departments_list.filter(d_name__icontains=query)
    paginator = Paginator(departments_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        departments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        departments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        departments = paginator.page(paginator.num_pages)
    return render(request, 'department/index.html', {'departments': departments})


def department_detail(request, d_slug):
    departments = get_object_or_404(Department, d_slug=d_slug)

    context = {
        'department': departments,
    }

    return render(request, 'department/detail.html', context)

@transaction.atomic
def department_create(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        try:
            with transaction.atomic():
                departments = form.save(commit=True)
                messages.success(request, "Department is created, successfully!")
                return HttpResponseRedirect(departments.get_department_url())
        except IntegrityError:
            messages.ValidationError(request, "Department is not created!")


    context = {
        'form': form,
    }
    return render(request, 'department/form.html', context)

@transaction.non_atomic_requests
def department_update(request, d_slug):
    departments = get_object_or_404(Department, d_slug=d_slug)
    form = DepartmentForm(request.POST or None, instance=departments)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, "Department is updated, successfully!")
        return HttpResponseRedirect(departments.get_updateD_url())
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
    projects_list = Project.objects.all()
    query = request.GET.get('q')
    if query:
        projects_list = projects_list.filter(p_title__icontains=query)
    paginator = Paginator(projects_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projects = paginator.page(paginator.num_pages)
    return render(request, 'project/index.html', {'projects': projects})


def project_detail(request, p_slug):
    projects = get_object_or_404(Project, p_slug=p_slug)
    context = {
        'project': projects,
    }

    return render(request, 'project/detail.html', context)

@transaction.atomic
def project_create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            with transaction.atomic:
                projects = form.save(commit=True)
                messages.success(request, "Project is created, successfully!")
                return HttpResponseRedirect(projects.get_project_url())
        except IntegrityError:
            messages.ValidationError(request, "Project is not created!")
    context = {
        'form': form,
    }
    return render(request, 'project/form.html', context)

@transaction.non_atomic_requests
def project_update(request, p_slug):
    projects = get_object_or_404(Project, p_slug=p_slug)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=projects)
    if form.is_valid():
        form.save(commit=True)
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

##########################################################

def issue_index(request):
    issues_list = Issue.objects.all()
    query = request.GET.get('q')
    if query:
        issues_list = issues_list.filter(i_id__icontains=query)
    paginator = Paginator(issues_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        issues = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        issues = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        issues = paginator.page(paginator.num_pages)
    return render(request, 'issue/index.html', {'issues': issues})


def issue_detail(request, id):
    issues = get_object_or_404(Issue, i_id=id)
    context = {
        'issue': issues,
    }

    return render(request, 'issue/detail.html', context)

@transaction.atomic
def issue_create(request):
    form = IssueForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            with transaction.atomic:
                issues = form.save(commit=True)
                messages.success(request, "Issue is created, successfully!")
                return HttpResponseRedirect(issues.get_issue_url())
        except IntegrityError:
            messages.ValidationError(request, "Issue is not created!")
    context = {
        'form': form,
    }
    return render(request, 'issue/form.html', context)

@transaction.non_atomic_requests
def issue_update(request, id):
    issues = get_object_or_404(Issue, i_id=id)
    form = IssueForm(request.POST or None, request.FILES or None, instance=issues)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, "Issue is updated, successfully!")
        return HttpResponseRedirect(issues.get_issue_url())
    context = {
        'form': form,
    }
    return render(request, 'issue/update.html', context)


def issue_delete(request, id):
    issues = get_object_or_404(Issue, i_id=id)
    issues.delete()
    return redirect('app:indexI')


##########################################################


def subtask_index(request):
    subtasks_list = Subtask.objects.all()
    query = request.GET.get('q')
    if query:
        subtasks_list = subtasks_list.filter(sub_id__icontains=query)
    paginator = Paginator(subtasks_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        subtasks = paginator.page(page)
    except PageNotAnInteger:
        subtasks = paginator.page(1)
    except EmptyPage:
        subtasks = paginator.page(paginator.num_pages)
    return render(request, 'subtask/index.html', {'subtasks': subtasks})


def subtask_detail(request, id):
    subtasks = get_object_or_404(Subtask, sub_id=id)
    context = {
        'subtask': subtasks,
    }

    return render(request, 'subtask/detail.html', context)

@transaction.atomic
def subtask_create(request):
    form = SubtaskForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            with transaction.atomic:
                subtasks = form.save()
                messages.success(request, "Subtask is created, successfully!")
                return HttpResponseRedirect(subtasks.get_subtask_url())
        except IntegrityError:
            messages.ValidationError(request, "Subtask is not created!")
    context = {
        'form': form,
    }
    return render(request, 'subtask/form.html', context)

@transaction.non_atomic_requests
def subtask_update(request, id):
    subtasks = get_object_or_404(Subtask, sub_id=id)
    form = SubtaskForm(request.POST or None, request.FILES or None, instance=subtasks)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, "Subtask is updated, successfully!")
        return HttpResponseRedirect(subtasks.get_subtask_url())
    context = {
        'form': form,
    }
    return render(request, 'subtask/update.html', context)


def subtask_delete(request, id):
    subtasks = get_object_or_404(Subtask, sub_id=id)
    subtasks.delete()
    return redirect('app:indexSub')


##########################################################
def head_index(request):
    employees_list = Employee.objects.filter(role='Head')
    query = request.GET.get('q')
    if query:
        employees_list = employees_list.filter(
            Q(e_name__icontains=query) |
            Q(e_surname__icontains=query) |
            Q(eDepartment__icontains=query)
            ).distinct()
    paginator = Paginator(employees_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        employees = paginator.page(paginator.num_pages)
    return render(request, 'employee/index.html', {'employees': employees})

##########################################################
def other_index(request):
    employees_list = Employee.objects.filter(role='Other')
    query = request.GET.get('q')
    if query:
        employees_list = employees_list.filter(
            Q(e_name__icontains=query) |
            Q(e_surname__icontains=query) |
            Q(eDepartment__icontains=query)
            ).distinct()
    paginator = Paginator(employees_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        employees = paginator.page(paginator.num_pages)
    return render(request, 'employee/index.html', {'employees': employees})
##########################################################
def company_view(request):
    #return HttpResponse('<b>Welcome</b>')
    return render(request, 'company/company.html', {})
##########################################################

##########################################################
def admin_view(request):
    #return HttpResponse('<b>Welcome</b>')
    return render(request, 'admin/admin.html', {})
