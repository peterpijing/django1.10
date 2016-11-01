#encoding:utf-8

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01.views import *
from books.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time/$',current_datetime,name= 'time'),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^search/$',search,name='serach'),
    url(r'^contact/$',contact),
    url(r'^image/$',my_image),

    #namespace TODO 1,这样导入子url后，我就不需要再引入app了
    url(r'^auth/', include('AUTH.urls',namespace='auth')),
    url(r'^cmdb/',include('CMDB.urls',namespace='cmdb')),
]
