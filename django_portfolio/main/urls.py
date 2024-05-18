from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("skills/", views.skills_page, name="skills-all"),
    path("skills/<int:id>", views.skills_page, name="skill"),
    path("experiences/", views.experience_page, name="experience-all"),
    path("experience/<int:id>", views.experience_page, name="experience"),
    path("projects/", views.project_page, name="projects"),
    path("project/<int:id>", views.project_page, name="project"),
    path("contact/", views.contact_page, name="contact"),
    path("git-profile/", views.git_profile_page, name="github-profile"),
]


# path("", views.home, name="home"),
# path("home/", views.home, name="home"),
# path("contact/", views.contact, name="contact"),
# path("project/<int:id>/", views.project, name="project"),