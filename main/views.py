from multiprocessing import context
from django.shortcuts import render, redirect

from .models import gallery
from .forms import galleryForm

# Create your views here.

def homePage(request):
    pictures = gallery.objects.all()
    form = galleryForm()

    # When form is submitted is part is excuted
    if request.method == 'POST':
        form = galleryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'pictures':pictures, 'form':form}
    return render(request, 'main/index.html', context)

def detail(request, pk):
    pictures = gallery.objects.get(pk=pk)
    context = {'pictures':pictures}
    return render(request, 'main/detail.html', context)