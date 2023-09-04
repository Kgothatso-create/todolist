from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskTitle (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']

class Task(models.Model):
    task_title = models.ForeignKey(TaskTitle, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    task_importance = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])

    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ['-complete']

class TaskDescription(models.Model):
    taskname = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_description = models.TextField(max_length=500)

    def __str__(self):
        return self.task_description
    
    def TaskDescription_count(self):
        return TaskDescription.objects.filter(taskname=self).count()