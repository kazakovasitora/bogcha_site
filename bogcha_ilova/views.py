from django.shortcuts import render

# Create your views here.

def bosh_sahifa(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')