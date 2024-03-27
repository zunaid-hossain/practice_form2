from django.shortcuts import render,redirect
from Album.models import Album
from musician.models import musician

def home(request):
    data=Album.objects.all()
    data1=musician.objects.all()

    info={'data1':data1}
    return render(request,'home.html',{'data':data})


