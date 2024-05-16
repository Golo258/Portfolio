from django.shortcuts import render
from .models import Project, ProjectImage, Tag


def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    images = ProjectImage.objects.all()
    context = {
        "projects": projects,
        "tags": tags,
        "images": images
    }
    return render(request,
                  "home.html",
                  context)


def contact(request):
    return render(request,
                  "contact.html",
                  {})


def project(request, id):
    return render(request,
                  "project.html",
                  {"id": id})
