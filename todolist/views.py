from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from .models import Todolist

from project.models import Project
from .forms import TodolistForm

def add(request, project_id):
    project = get_object_or_404(Project, pk=project_id, created_by=request.user)
    
    if request.method == 'POST':
        form = TodolistForm(request.POST)
        
        if form.is_valid:
            todolist = form.save(commit=False)
            todolist.project = project
            todolist.created_by = request.user
            
            todolist.save()
            
            return redirect(f'/projects/{project_id}/')
    else:
        form = TodolistForm()
        
    return render(request, 'todolist/add.html', {'form':form, 'project':project})
            