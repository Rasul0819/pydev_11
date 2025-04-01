from django.shortcuts import render,get_object_or_404
from . import models
# Create your views here.
def homepage(request):
    telefonlar = models.Mobi.objects.all()#bazadagi zatlardin hammesi
    return render(request,'home.html',{'telefonlar':telefonlar})


def detail(request,id):
    telefon = get_object_or_404(models.Mobi,id=id)
    return render(request,'detail.html',{'telefon':telefon})


