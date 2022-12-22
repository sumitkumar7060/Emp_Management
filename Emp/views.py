from django.shortcuts import render, redirect
from . models import *

# Create your views here.


def index(request):
    return render(request, "home.html")


def add(request):
    return render(request, 'add.html')


def show(request):
    return render(request, 'show.html')


def data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        mobile = request.POST.get('mobile')
        manager = request.POST.get('manager')
        office = request.POST.get('office')
        join_date = request.POST.get('joindate')

        s = Employee(
            Name=name,
            Role=role,
            Mobile=mobile,
            Manager=manager,
            Office=office,
            Joining_date=join_date
        )
        s.save()
        return redirect('home')


def show(request):
    ss = Employee.objects.all()
    # print(ss)
    return render(request, 'home.html', {"look": ss})
