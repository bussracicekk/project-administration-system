from django.conf.urls import url
from .views import *

app_name = 'app'

urlpatterns = [

    url(r'^employees/$', employee_index, name='index'),
    url(r'^employee/add/$', employee_create, name='create'),
    url(r'^(?P<e_slug>[\w-]+)/detail/$', employee_detail, name='detail'),
    url(r'^(?P<e_slug>[\w-]+)/update/$', employee_update, name='update'),
    url(r'^(?P<e_slug>[\w-]+)/delete/$', employee_delete, name='delete'),

    url(r'^departments/$', department_index, name='indexD'),
    url(r'^department/add/$', department_create, name='createD'),
    url(r'^(?P<d_slug>[\w-]+)/detailD/$', department_detail, name='detailD'),
    url(r'^(?P<d_slug>[\w-]+)/updateD/$', department_update, name='updateD'),
    url(r'^(?P<d_slug>[\w-]+)/deleteD/$', department_delete, name='deleteD'),

    url(r'^projects/$', project_index, name='indexP'),
    url(r'^project/add/$', project_create, name='createP'),
    url(r'^(?P<p_slug>[\w-]+)/detailP/$', project_detail, name='detailP'),
    url(r'^(?P<p_slug>[\w-]+)/updateP/$', project_update, name='updateP'),
    url(r'^(?P<p_slug>[\w-]+)/deleteP/$', project_delete, name='deleteP'),

]
