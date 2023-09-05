"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from list import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logOutUser, name = 'logout'),
    
    path('list_of_tasks/<int:TaskTitle_id>/', views.see_list_of_tasks, name='list_of_tasks'),
    path('task_details/<int:Task_id>/', views.see_task_details, name='task_details'),

    path('create/', views.create_title, name='create'),
    
    path('delete_task/<int:TaskTitle_id>/', views.delete_task, name='delete_task'),

    path('delete_task_details/<int:TaskDescription_id>/', views.delete_task_details, name='delete_task_details'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),

]

