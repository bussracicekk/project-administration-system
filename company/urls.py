from django.conf.urls import url
from .views import *


app_name = 'employee'
app_name = 'department'

urlpatterns = [

    url(r'^employees/$', employee_index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', employee_detail, name="detail"),
    url(r'^employee/add/$', employee_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', employee_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', employee_delete, name='delete'),

    url(r'^departments/$', department_index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', department_detail, name="detail"),
    url(r'^department/add/$', department_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', department_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', department_delete, name='delete'),
]
