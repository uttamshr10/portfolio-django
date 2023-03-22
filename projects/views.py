from django.shortcuts import render
from projects import models
# Create your views here.
def homepage(request):
    projects = models.Project.objects
    return render(request, 'projects/index.html', {'projects':projects})
