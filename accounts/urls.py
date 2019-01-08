from django.conf.urls import url
from .views import *

app_name = 'account'

urlpatterns = [

    url(r'^login/$', login_view, name='login'),
]