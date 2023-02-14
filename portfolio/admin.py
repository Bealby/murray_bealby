from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'github',
        'website', 
        'image',
        'code',
        'description',
    )


admin.site.register(Project, ProjectAdmin)
