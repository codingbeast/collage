from iptools import views
from django.urls import path
from django.conf.urls import url,include

app_name = 'iptools'

urlpatterns = [
    url(r'^$',views.home,name="home"),
]
