from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jumia(request):
    # return HttpResponse("<h1>Welcome to my home page<h1/>")
    return render(request, "jumia/jumiaapp.html")
