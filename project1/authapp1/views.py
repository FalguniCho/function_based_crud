from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

def signup(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginv_url')
    template_name='authapp1/signup.html'
    context={'form':form}
    return render(request,template_name,context)

def loginv(request):
    if request.method == 'POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')

        user = authenticate(username=un,password=pw)

        if user is not None:
            login(request,user)
            return redirect('show_url')

    template_name='authapp1/login.html'
    context={}
    return render(request,template_name,context)

def logoutv(request):
    logout(request)
    return redirect('loginv_url')


