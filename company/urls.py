from django.conf.urls import url
from .views import *


app_name = 'app'


urlpatterns = [

    url(r'^employees/$', employee_index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', employee_detail, name="detail"),
    url(r'^employee/add/$', employee_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', employee_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', employee_delete, name='delete'),

    url(r'^departments/$', department_index, name='indexD'),
    url(r'^(?P<id>\d+)/detailD/$', department_detail, name="detailD"),
    url(r'^department/add/$', department_create, name='createD'),
    url(r'^(?P<id>\d+)/updateD/$', department_update, name='updateD'),
    url(r'^(?P<id>\d+)/deleteD/$', department_delete, name='deleteD'),
]
