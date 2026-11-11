from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from .forms import *
from .models import *

def Index(req):
    form=Employee_form()
    
    if req.method=='POST':
        form=Employee_form(req.POST)
        if form.is_valid():
            form.save()
    Emp_data=Employee.objects.all()
    context={
        'forms':form,
        'Emp_data':Emp_data,
        
    }
    return render(req,'Index.html',context)


def update(req,pk):
    employee=get_object_or_404(Employee,id=pk)
    
    if req.method=='POST':
        form=Employee_form(req.POST,instance=employee)
        form.save()
        return redirect('index_page')
        
    else:
        form=Employee_form(instance=employee)
    context={
        'forms':form
    }
    return render(req,'Update.html',context)



def delete(req,pk):
    employee=get_object_or_404(Employee,id=pk)
    form=Employee_form(instance=employee)
    if req.method=='POST':
        employee.delete()
        return redirect('index_page')
    else:
        form=Employee_form(instance=employee)
    context={
        'forms':form
    }
    return render(req,'Delete.html',context)