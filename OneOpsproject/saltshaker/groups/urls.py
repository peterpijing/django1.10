from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^manage_group', views.manage_group,name='manage_group'),
    url(r'^manage_host', views.manage_host,name='manage_host'),
    url(r'^del_group', views.del_group,name='del_group'),
    url(r'^add_group', views.add_group,name='add_group'),
    url(r'^modify_group', views.modify_group,name='modify_group'),
    url(r'^add_host', views.add_host,name='add_host'),
    url(r'^del_host', views.del_host,name='del_host'),
]