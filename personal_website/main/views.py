from django.shortcuts import render
from .models import Project, Skill

def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def skills(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'skills.html', context)

def about(request):
    return render(request, 'about.html')
