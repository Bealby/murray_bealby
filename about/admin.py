from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description_1',
        'description_2',
        'hobbie_1', 
        'hobbie_2', 
        'hobbie_3', 
        'hobbie_4', 
    )


admin.site.register(About, AboutAdmin)
