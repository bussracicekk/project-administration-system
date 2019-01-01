from django.conf.urls import url
from .views import *


app_name = 'employee'


urlpatterns = [

    url(r'^employees/$', employee_index),
    url(r'^(?P<id>\d+)/$', employee_detail, name="detail"),
    url(r'^add/$', employee_create),

]
