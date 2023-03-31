from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required
@login_required(login_url='loginv_url')
def addv(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name='app1/add.html'
    context={'form':form}
    return render(request, template_name, context)
@login_required(login_url='loginv_url')
def showv(request):
    data = Student.objects.all()
    template_name='app1/show.html'
    context={'objs': data}
    return render(request, template_name, context)

def updatev(request,op):
    obj = Student.objects.get(id=op)
    form=StudentForm(instance=obj)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name='app1/add.html'
    context={'form':form}
    return render(request,template_name, context)

def deletev(request,op):
    obj=Student.objects.get(id=op)
    if request.method=='POST':
        obj.delete()
        return redirect('show_url')
    template_name='app1/delete.html'
    context={'obj':obj}
    return render(request, template_name, context)
from django.shortcuts import render

# Create your views here.
