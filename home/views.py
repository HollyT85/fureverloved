from django.shortcuts import render

def index(request):
    # Home Page
    return render(request, 'home/index.html')