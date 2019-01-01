from django import forms
from .models import Employee
from .models import Department


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
        ]
        
        
class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = [
            'd_id',
            'd_name',
            'd_capacity',
            'd_password',
            'dCompany',
        ]
