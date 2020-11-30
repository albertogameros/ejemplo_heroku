from django.shortcuts import render

# Create your views here.

def home(request):
    """
    docstring
    """
    return render(request,'home.html')