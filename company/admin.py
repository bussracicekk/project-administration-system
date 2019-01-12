from django.contrib import admin
from .models import Company
from .models import Employee
from .models import Department
from .models import Project
from .models import Issue
from .models import Subtask
from .models import Helps
from .models import ForeignCompany

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Subtask)
admin.site.register(Helps)
admin.site.register(ForeignCompany)
