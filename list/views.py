from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, TaskTitleForm, TaskForm, TaskDescriptionForm, EditTaskForm
from django.contrib import messages
from .models import Task,TaskDescription,TaskTitle

from django.contrib.auth import authenticate, login, logout

# Create your views here.

#Register view
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

# login view
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

#logout view
def logOutUser(request):
    logout(request)
    return redirect ('login')


# task views here

#task home here
def index (request):
    user=request.user
    task_title = TaskTitle.objects.filter(user=user)
    username = user.username
    context = {'task_title':task_title, 'username':username}
    return render(request,'index.html', context)

# list of tasks under a tast title
def see_list_of_tasks(request,TaskTitle_id):
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

# delete single task
def delete_task(request, task_id):
    pass

# a single tasks details view and edit
def see_task_details(request, Task_id):
    task = get_object_or_404(Task, pk=Task_id)
    taskname = task.task_name
    existing_details = TaskDescription.objects.filter(taskname=task).first()  # Get existing details if they exist

    if request.method == 'POST':
        task_details_form = TaskDescriptionForm(request.POST, instance=existing_details)
        if task_details_form.is_valid():
            task_description = task_details_form.save(commit=False)
            task_description.taskname = task  # Assign the taskname
            task_description.save()
            return redirect('task_details', Task_id=Task_id)  # Redirect back to task details page after editing

    else:
        if existing_details:
            # If there are existing details, initialize the form with them for viewing/editing
            task_details_form = TaskDescriptionForm(instance=existing_details)
        else:
            # If there are no existing details, create a new form for adding
            task_details_form = TaskDescriptionForm()

    context = {'taskname': taskname, 'details': existing_details, 'task_details_form': task_details_form}
    return render(request, 'taskdetails.html', context)

# delete task details
def delete_task_details(request, TaskDescription_id):
    task_description = get_object_or_404(TaskDescription, pk=TaskDescription_id)

    if request.method == 'POST':
        # Get the related task using the task_description's foreign key
        task = task_description.taskname

        # Delete the task detail
        task_description.delete()
        
        # Redirect to the task details page or any other appropriate URL
        return redirect('task_details', Task_id=task.id)  # Assuming 'task_details' is the URL pattern for viewing task details

    # Render the template with the form
    return render(request, 'delete_task_details.html', {'task_description': task_description})

# create a task title
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

# delete list of tasks by deleting the task title
def delete_task(request, TaskTitle_id):
    task_title = get_object_or_404(TaskTitle, pk=TaskTitle_id)

    if request.method == 'POST':
        # Delete all tasks associated with the title
        task_title.delete()
        return redirect('index')
    else:

        context = {'task_title': task_title}
        return render(request, 'tasklist.html', context)
    
# update title
def update_title(request , tasktitle_id):
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