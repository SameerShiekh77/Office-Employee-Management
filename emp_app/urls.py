from django.contrib import admin
from django.urls import path,include
from . import views
from .sitemaps import EmpSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "emps" : EmpSitemap,
    'static': StaticViewSitemap

}


urlpatterns = [
    path("",views.index,name='index'),
    path("view_emp/",views.view_emp,name='view_emp'),
    path("add_emp/",views.add_emp,name='add_emp'),
    path("dlt_emp/<int:id>/",views.dlt_emp,name='dlt_emp'),
    path("filter_emp/",views.filter_emp,name='filter_emp'),
    path("sitemap.xml/",sitemap, {"sitemaps":sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path("emp/<int:id>/",views.emp,name='emp'),
    path('accounts/login/',views.login,name='login')

]
