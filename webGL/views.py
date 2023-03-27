from django.shortcuts import render, redirect

# Create your views here.
def welcome(request):
    return render(request, "webGL/welcome.html")

def unit(request):
    return render(request, "webGL/index.html")