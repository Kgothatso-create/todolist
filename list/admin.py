from django.contrib import admin
from .models import TaskTitle, Task, TaskDescription  # Import your models here

# Register your models here.
admin.site.register(TaskTitle)
admin.site.register(Task)
admin.site.register(TaskDescription)

