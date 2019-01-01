from django import forms
from .models import Employee


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
        ]
