from django.shortcuts import render, redirect

from .models import Gallery
from .forms import GalleryForm

# Create your views here.

def homePage(request):
    pictures = Gallery.objects.all()
    context = {'pictures':pictures}
    return render(request, 'main/index.html', context)

def detail(request, pk):
    pictures = Gallery.objects.get(pk=pk)
    context = {'pictures':pictures}
    return render(request, 'main/detail.html', context)

def add(request):
    # When form is submitted
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form = GalleryForm()
    context = {'form':form}
    return render(request, 'main/add.html', context)