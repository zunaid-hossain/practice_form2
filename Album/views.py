from django.shortcuts import render,redirect
from .import forms
from .models import Album
def home(request):

    if request.method=="POST":
        album=forms.AlbumForm(request.POST)
        if album.is_valid():
            album.save()
            return redirect('home')
    else:
        album=forms.AlbumForm()

    return render(request,'album.html',{'form':album})


def delete(request,id):
    album= Album.objects.get(pk=id)
    album.delete()
    return redirect('home')

def edit(request,id):
    album= Album.objects.get(pk=id)
    AlbumFrom=forms.AlbumForm(instance=album)
    if request.method=="POST":
        album=forms.AlbumForm(request.POST,instance=album)
        if album.is_valid():
            album.save()
            return redirect('home')
        
    return render(request,'album.html',{'form':AlbumFrom})
