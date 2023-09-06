from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Use the correct template path
