from django.shortcuts import render
from .models import *

# Create your views here.


def homePage(request):
    context=contextReturn()
    home=HomePage.objects.all().first()
    context_2={
        'home':home
    }
    context.update(context_2)
    return render(request,"website/home.html",context=context)

def fenster(request):
    context=contextReturn()
    fenster=FensterPage.objects.all().first()
    context_2={
        'fenster':fenster
    }
    context.update(context_2)
    return render(request,"website/fenster.html",context=context)

def kunAluFenster(request):
    context=contextReturn()
    alufenster=KunAluFensterPage.objects.all().first()
    context_2={
        'alufenster':alufenster
    }
    context.update(context_2)
    return render(request,"website/kunAluFenster.html",context=context)

def holzAluFenster(request):
    context=contextReturn()
    holzalufenster=HolzAluFenster.objects.all()
    context_2={
        'holzalufenster':holzalufenster
    }
    context.update(context_2)
    return render(request,"website/holzAluFenster.html",context=context)

def holzfenster(request):
    context=contextReturn()
    holzfenster=HolzFenster.objects.all()
    context_2={
        'holzfenster':holzfenster
    }
    context.update(context_2)
    return render(request,"website/holzfenster.html",context=context)

def turen(request):
    context=contextReturn()
    turen=TurenPage.objects.all().first()
    context_2={
        'turen':turen
    }
    context.update(context_2)
    return render(request,"website/tueren.html",context=context)

def sonnen(request):
    context=contextReturn()
    return render(request,"website/sonnen-und-insektenschutz.html",context=context)

def toranlagen(request):
    context=contextReturn()
    langen=ToranLagenPage.objects.all().first()
    context_2={
        'langen':langen
    }
    context.update(context_2)
    return render(request,"website/toranlagen.html",context=context)

def kontakt(request):
    context=contextReturn()
    return render(request,"website/kontakt.html",context=context)

def Datenschutzerklärung(request):
    context=contextReturn()
    return render(request,"website/Datenschutzerklärung.html",context=context)

def impressum(request):
    context=contextReturn()
    return render(request,"website/impressum.html",context=context)








def contextReturn():
    number=PhoneNumber.objects.all().first()
    openingHours=OpeningHours.objects.all()
    location=Location.objects.all().first()
    email=Email.objects.all().first()
    map_link=Map.objects.all().first()
    context={
        'number':number,
        'openingHours':openingHours,
        'location':location,
        'email':email,
        'map_link':map_link
    }
    return context