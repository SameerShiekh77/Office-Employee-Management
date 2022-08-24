from django.urls import path
from .views import EmployeeList, EmployeeDetail

app_name = 'blog_api'

urlpatterns = [
    path('api/<int:pk>/', EmployeeDetail.as_view(), name='detailcreate'),
    path('api/', EmployeeList.as_view(), name='listcreate'),
]