from django.shortcuts import render
from .models import Jamoa, Lesson
from django.core.mail import send_mail
# Create your views here.

def bosh_sahifa(request):
    darslar = Lesson.objects.all()
    uqituvchilar=Jamoa.objects.all()
    return render(request, 'indexx.html', {"Html_Dars": darslar, "Uqituvchi":uqituvchilar})

def about(request):
    uqituvchilar=Jamoa.objects.all()
    return render(request, 'about.html',{"Uqituvchi":uqituvchilar})

def blok(request):
    return render(request, 'blog.html')

def klas(request):
    darslar = Lesson.objects.all()
    return render(request, 'class.html', {"Html_Dars": darslar})

def kontakt(request):
    if request.method == 'POST':
        ism = request.POST['ism']
        email = request.POST['pochta']
        xabar = request.POST['mess']
        mavzu = request.POST['mavzu']
        title=ism
        msg='Sizga '+ism+'dan xabar bor'+'\nPochtasi: '+email+'\nMavzusi:'+mavzu+'\nXabari:\n'+xabar

        print(ism, xabar, email)
        send_mail(
            ism,
            msg,
            email,
            ['kazakovasitora06@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'contact.html')

def galery(request):
    return render(request, 'gallery.html')

def sing(request):
    return render(request, 'single.html')

def team1(request):
    uqituvchilar=Jamoa.objects.all()
    return render(request, 'team.html',{"Uqituvchi":uqituvchilar})