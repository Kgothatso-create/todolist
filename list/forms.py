from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task,TaskDescription,TaskTitle
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskTitleForm(forms.ModelForm):
    class Meta:
        model = TaskTitle
        fields = ['title']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','task_importance']

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','complete','task_importance']

class TaskDiscriptionForm(forms.ModelForm):
    class Meta:
        model = TaskDescription
        fields = ['task_description']