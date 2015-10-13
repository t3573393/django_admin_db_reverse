#coding:utf8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save_db_info/$', views.save_db_info, name='save_db_info'),
    url(r'^table_list/$', views.table_list, name='table_list'),
    url(r'^generate_code/$', views.generate_code, name='generate_code'),
]