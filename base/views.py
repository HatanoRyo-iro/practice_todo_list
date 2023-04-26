from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView

# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
        