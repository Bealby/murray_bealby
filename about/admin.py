from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description_1',
        'description_2',
        'hobby_1',
        'hobby_2',
        'hobby_3',
        'hobby_4',
    )


admin.site.register(About, AboutAdmin)
