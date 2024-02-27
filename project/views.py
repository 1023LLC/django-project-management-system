from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ProjectForm
from django.shortcuts import render, get_object_or_404
from .models import Project
from django.contrib.auth.decorators import login_required


@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    
    return render(request, 'project/projects.html', {'projects':projects})



@login_required
def project(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    
    return render(request, 'project/project.html', {'project':project})




@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, 'Project added successfully.')
            return HttpResponseRedirect(reverse('project:projects'))
        else:
            messages.error(request, 'Form is not valid. Please check the data.')
    else:
        form = ProjectForm()
    return render(request, 'project/add.html', {'form': form})