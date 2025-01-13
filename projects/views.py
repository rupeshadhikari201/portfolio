from django.shortcuts import render
from .models import Projects

# Create your views here.
def projects(request):
    projects = Projects.objects.all()
    print(projects)
    return render(request, 'projects/projects.html', {'projects' : projects})