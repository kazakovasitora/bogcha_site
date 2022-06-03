from django.shortcuts import render
from .models import Lesson
# Create your views here.

def bosh_sahifa(request):
    darslar = Lesson.objects.all()
    return render(request, 'index.html', {"Html_Dars": darslar})
def about(request):
    return render(request, 'about.html')
def blok(request):
    return render(request, 'blog.html')
def klas(request):
    darslar = Lesson.objects.all()
    return render(request, 'class.html', {"Html_Dars": darslar})
def kontakt(request):
    return render(request, 'contact.html')
def galery(request):
    return render(request, 'gallery.html')
def sing(request):
    return render(request, 'single.html')
def team1(request):
    return render(request, 'team.html')