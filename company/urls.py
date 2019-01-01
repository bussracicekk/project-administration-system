from django.conf.urls import url
from .views import *


app_name = 'employee'


urlpatterns = [

    url(r'^employees/$', employee_index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', employee_detail, name="detail"),
    url(r'^employee/add/$', employee_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', employee_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', employee_delete, name='delete'),

]
