from django.shortcuts import render

def index(request):
    return render(request,'index.html')
# Create your views here.

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'about.html')

def cycle(request):
    return render(request,'cycle.html')

def news(request):
    return render(request,'news.html')