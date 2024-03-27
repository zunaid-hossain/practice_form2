from django.shortcuts import render,redirect
from .import forms
from .models import musician
# Create your views here.
def home(request):
   if request.method=="POST":
      album=forms.musicianForm(request.POST)
      if album.is_valid():
         album.save()
         return redirect('home')
   else:
      album=forms.musicianForm()
   
   return render(request,'musician.html',{"form":album}) 

def edit(request,id):
   m=musician.objects.get(pk=id)
   mFrom=forms.musicianForm(instance=m)
   if request.method=="POST":
      album=forms.musicianForm(request.POST,instance=m)
      if album.is_valid():
         album.save()
         return redirect('home')
   
   return render(request,'musician.html',{"form":mFrom}) 
