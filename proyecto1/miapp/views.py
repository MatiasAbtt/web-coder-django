from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"nombre" : "Matias Abtt"}
    return render(request, "index.html", context)