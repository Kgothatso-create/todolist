from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, TaskTitleForm, TaskForm, TaskDiscriptionForm, EditTaskForm
from django.contrib import messages
from .models import Task,TaskDescription,TaskTitle

from django.contrib.auth import authenticate, login, logout

# Create your views here.


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

# task views here
def index (request):
    user=request.user
    task_title = TaskTitle.objects.filter(user=user)
    username = user.username
    context = {'task_title':task_title, 'username':username}
    return render(request,'index.html', context)

def list_of_tasks(request,TaskTitle_id):
    task_title = get_object_or_404(TaskTitle, pk=TaskTitle_id)
    tasks = Task.objects.filter(task_title=task_title)
    task_form = TaskForm()

    if request.method == 'POST':
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.task_title = task_title  
            new_task.save()

            return redirect('list_of_tasks', TaskTitle_id=TaskTitle_id)
    else:
        task_form = TaskForm()

    context = {'tasks':tasks,'task_title':task_title, 'task_form': task_form }
    return render(request, 'tasklist.html', context)

def task_details(request,Task_id):
    taskname = get_object_or_404(Task, pk=Task_id)
    details = TaskDescription.objects.filter(taskname=taskname)

    context = {'taskname':taskname, 'details':details}

    return render(request,'taskdetails.html', context)

def create_title(request):
    if request.method == 'POST':
        title_form = TaskTitleForm(request.POST)

        if title_form.is_valid():
            
            new_title = title_form.save()
            new_title.user = request.user
            new_title.save()

            return redirect('list_of_tasks', TaskTitle_id=new_title.id)
    else:
        title_form = TaskTitleForm()

    context = {'title_form': title_form}
    return render(request, 'addtodo.html', context)

def add_task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    task_details_form = EditTaskForm()

    if request.method == 'POST':
        task_details_form = EditTaskForm(request.POST, instance=task)
        if task_details_form.is_valid():
            task_details_form.save()
            
            return redirect('taskdetails')  
    else:
        task_details_form = EditTaskForm(instance=task)

    return render(request, 'addtaskdetail.html', {'task_details_form': task_details_form, 'task': task})