from django.shortcuts import render

def about(request):
    # Home Page
    return render(request, 'about/about.html')