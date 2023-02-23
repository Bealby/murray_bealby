from django.shortcuts import render
from .models import About


def about_content(request):
    """ A view to show all projects """

    about = About.objects.all()

    context = {
        'about': about,
    }

    return render(request, 'about/about.html', context)
