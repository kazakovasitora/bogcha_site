from django.shortcuts import render

# Create your views here.

def bosh_sahifa(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blok(request):
    return render(request, 'blog.html')
def klas(request):
    return render(request, 'class.html')
def kontakt(request):
    return render(request, 'contact.html')
def galery(request):
    return render(request, 'gallery.html')
def sing(request):
    return render(request, 'single.html')
def team1(request):
    return render(request, 'team.html')