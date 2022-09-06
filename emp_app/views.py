import imp
from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .models import Role, Department, Employee
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")


def view_emp(request):
  
    emps = Employee.objects.all()
    # pagination vofr
    paginator = Paginator(emps,5)
    page_number = request.GET.get('page')
    finalPage = paginator.get_page(page_number)
    context = {
        'emps':finalPage
    }
    return render(request,"view_emp.html",context)

@login_required
def add_emp(request):
    
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        depart = request.POST.get('depart')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role = request.POST.get('role')
        phone = request.POST.get('phone')    
        EmpObj = Employee(first_name=firstName,last_name=lastName,depart_id=depart,salary=salary,bonus=bonus,role_id=role,phone=phone,hireDate=datetime.now())
        EmpObj.save()

        return redirect(add_emp)
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Error!!!")

        
    return render(request,"add_emp.html")

@login_required
def dlt_emp(request,id):
    
    empObj = Employee.objects.get(id=id)
    empObj.delete()
    return HttpResponse("Employee Deleted Successfully!! <br><a href='/view_emp'>Back to Employee List</a>")


@login_required
def filter_emp(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        depart = request.POST.get('depart')
        role = request.POST.get('role')
        emps = Employee.objects.all()
        if emps:
            emps = emps.filter(Q(first_name__icontains=fullname) or Q(last_name__icontains=fullname))
        if depart:
            emps = emps.filter(Q(depart__id=depart))
        if role:
            emps = emps.filter(Q(role__id=role))

        context = {
            'emps':emps
        }
        return render(request,"view_emp.html",context)
    
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    # else:
    #     return HttpResponse("An Exception Occurred")
    
    return render(request,"filter_emp.html")


def emp(request):
    pass


def login(request):
    return render(request, 'login.html')