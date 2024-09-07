from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def choice(request):
    # return HttpResponse("<h3>Welcome! kindly, make your pick from our list of available items<h3/>")
    return render(request, "choice/choice.html")
