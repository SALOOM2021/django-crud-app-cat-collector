from django.shortcuts import render
# Import HttpResponse to send text-based responses
from .models import Cat

def home(request):
    # Send a simple HTML response
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


def cat_index(request):
    cats = Cat.objects.all()
    # Render the cats/index.html template with the cats data
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})