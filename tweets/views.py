from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page of the Blog"""
    return render(request, 'tweets/index.html')
