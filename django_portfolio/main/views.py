from django.shortcuts import render, get_object_or_404
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
    project = get_object_or_404(Project, pk=id)
    return render(request,
                  "project.html",
                  {"project": project})
