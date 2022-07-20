from django.contrib import admin
from .models import Employee,Role, Department
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","depart","salary","bonus","role","phone")

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",'location') 

    

admin.site.register(Role)