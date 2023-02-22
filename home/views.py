from django.shortcuts import render


def index(request):
    """A view to returnindex page"""

    return render(request, 'home/index.html')
