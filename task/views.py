from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from project.models import Project
from todolist.models import Todolist
from .models import Task
from .forms import TaskForm


@login_required
def add(request, project_id, todolist_id):
    
    project = get_object_or_404(Project, pk=project_id, created_by=request.user)
    todolist = get_object_or_404(Todolist, project=project, pk=todolist_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid:
            task = form.save(commit=False)
            task.created_by = request.user
            task.project = project
            task.todolist = todolist
            task.save()
            
            
            return redirect(f'/projects/{project_id}/{todolist_id}/')
    else:
        form = TaskForm()
        
    return render(request, 'task/add.html', {'form': form, 'project': project, 'todolist': todolist})