from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save_db_info/$', views.save_db_info, name='save_db_info'),
]