from django.contrib import admin
from .models import Employee
from company.models import Employee
from .models import Company

admin.site.register(Employee)


admin.site.register(Company)

