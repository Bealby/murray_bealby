from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'github',
        'website',
        'image_front',
        'image_back',
        'code',
        'crud',
        'letter',
        'description',
        'position',
        'api',
    )


admin.site.register(Project, ProjectAdmin)
