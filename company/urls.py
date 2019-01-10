from django.conf.urls import url
from .views import *

app_name = 'app'

urlpatterns = [

    url(r'^home/$', company_view, name='homeC'),

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

    url(r'^issues/$', issue_index, name='indexI'),
    url(r'^issue/add/$', issue_create, name='createI'),
    url(r'^(?P<i_slug>[\w-]+)/detailI/$', issue_detail, name='detailI'),
    url(r'^(?P<i_slug>[\w-]+)/updateI/$', issue_update, name='updateI'),
    url(r'^(?P<i_slug>[\w-]+)/deleteI/$', issue_delete, name='deleteI'),

    url(r'^subtasks/$', subtask_index, name='indexSub'),
    url(r'^subtask/add/$', subtask_create, name='createSub'),
    url(r'^(?P<sub_slug>[\w-]+)/detailSub/$', subtask_detail, name='detailSub'),
    url(r'^(?P<sub_slug>[\w-]+)/updateSub/$', subtask_update, name='updateSub'),
    url(r'^(?P<sub_slug>[\w-]+)/deleteSub/$', subtask_delete, name='deleteSub'),

]
