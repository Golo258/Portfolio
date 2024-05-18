from django.contrib import admin
from .models import (Tag, 
                     Project, 
                     ProjectImage,
                     Experience,
                     Skill,
                     Localization)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date")
    search_fields = ("position", "company")
    list_filter = ("start_date", "end_date")

class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    search_fields = ("name", )
    list_filter = ("level",) 

admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Localization)
