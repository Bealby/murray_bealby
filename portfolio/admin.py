from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'github',
        'website', 
        'image_front',
        'image_back',
        'code',
        'description',
        'position',
    )


admin.site.register(Project, ProjectAdmin)
