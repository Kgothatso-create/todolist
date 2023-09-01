from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index (request):
    context = {}
    return render(request,'index.html', context)

def registerPage (request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Welcome ' + user)
            context = {}
            redirect('index')
        
            
    context = {'form':form}
    return render(request, "register.html", context)

def loginPage (request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, 'Username or Password Inccorect')
            
            return render(request,'login.html')


    context = {}
    return render(request,'login.html', context)

def logOutUser(request):
    logout(request)
    return redirect ('login')