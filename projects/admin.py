from django.contrib import admin
from projects.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "technology", "date_created"]

admin.site.register(Project, ProjectAdmin)

