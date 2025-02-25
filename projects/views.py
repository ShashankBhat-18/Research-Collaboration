from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm


@login_required
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def project_create(request):
    if request.user.user_type != 'professor':
        messages.error(request, 'Only professors can create projects.')
        return redirect('projects:project_list')

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.professor = request.user
            project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('projects:project_list')
    else:
        form = ProjectForm()

    return render(request, 'projects/project_form.html', {'form': form})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})
