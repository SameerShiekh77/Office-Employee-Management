
from tkinter.font import names
from unicodedata import name
from xml.dom.expatbuilder import Namespaces
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("view_emp/",views.view_emp,name='view_emp'),
    path("add_emp/",views.add_emp,name='add_emp'),
    path("dlt_emp/<int:id>/",views.dlt_emp,name='dlt_emp'),
    path("filter_emp/",views.filter_emp,name='filter_emp'),
    path("api-auth/",include('rest_framework.urls',namespace="rest_framework"))
]
