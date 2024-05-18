from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage, Tag


def home_page(request):
    return render(request, "home_page.html", {})


def skills_page(request):
    return render(request, "skills_page.html", {})


def experience_page(request):
    return render(request, "experience_page.html", {})


def project_page(request):
    return render(request, "project_page.html", {})


def contact_page(request):
    return render(request, "contact_me_page.html", {})


def git_profile_page(request):
    return render(request, "gitProfile_page.html", {})


# def home(request):
#     projects = Project.objects.all()
#     tags = Tag.objects.all()
#     images = ProjectImage.objects.all()
#     context = {
#         "projects": projects,
#         "tags": tags,
#         "images": images
#     }
#     return render(request,
#                   "home.html",
#                   context)
#
#
# def contact(request):
#     return render(request,
#                   "contact.html",
#                   {})
#
#
# def project(request, id):
#     project = get_object_or_404(Project, pk=id)
#     project.description = project.description.split("\n")
#     context = {"project" : project}
#
#     return render(request,
#                   "project.html",
#                   context)

# ----------------------------
