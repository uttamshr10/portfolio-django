from django.shortcuts import render, get_object_or_404
from .models import Project
# Create your views here.
def homepage(request):
    projects = Project.objects
    context = {
        'projects' : projects
    }
    return render(request, 'projects/index.html', context)

def detail(request, pk):
    project_detail = get_object_or_404(Project, pk=pk)
    context = {
        'project' : project_detail
    }
    return render(request, 'projects/detail.html', context)
