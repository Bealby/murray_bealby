from django.shortcuts import render

# Create your views here.

def index (request):
    """A view to returnindex page"""

    return render(request, 'home/index.html')
