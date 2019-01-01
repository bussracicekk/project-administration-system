from django.conf.urls import url
from .views import *


app_name = 'employee'


urlpatterns = [

    url(r'^employees/$', employee_index),
    url(r'^(?P<id>\d+)/detail/$', employee_detail, name="detail"),
    url(r'^employee/add/$', employee_create),
    url(r'^(?P<id>\d+)/update/$', employee_update),

]
