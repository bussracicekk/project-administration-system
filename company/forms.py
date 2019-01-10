from django import forms
from .models import Employee
from .models import Department
from .models import Project
from .models import Issue
from .models import Subtask


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            'e_id',
            'e_name',
            'e_surname',
            'e_password',
            'e_email',
            'e_phone',
            'e_degree',
            'e_salary',
            'eCompany',
            'eDepartment',
            'Image'
        ]
        
        
class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = [
            'd_id',
            'd_name',
            'd_capacity',
            'd_phone',
            'd_password',
            'dCompany',
        ]


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'p_id',
            'p_startdate',
            'p_enddate',
            'p_title',
            'p_situation',
            'cProject',
            'dProject',
            'eProject',
            'image',
        ]


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = [
            'i_id',
            'i_type',
            'i_extra',
            'i_content',
            'pIssue',
            'i_work',
        ]

class SubtaskForm(forms.ModelForm):

    class Meta:
        model = Subtask
        fields = [
            'sub_id',
            'sub_content',
            'iIssue',
            's_work',
        ]