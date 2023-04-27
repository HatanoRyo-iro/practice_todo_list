from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_detail.html'
    

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_create_form.html'
    success_url = reverse_lazy('tasks')
    

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
    
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('tasks')
    