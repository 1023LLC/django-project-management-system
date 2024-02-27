from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Project


@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    
    return render(request, 'project/projects.html', {'projects':projects})


@login_required
def add_project(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        
        if name:
            Project.objects.create(name=name, description=description, created_by=request.user)
            
            return redirect('/projects/')
        else:
            print('Not valid!')    
    return render(request, 'project/add.html')