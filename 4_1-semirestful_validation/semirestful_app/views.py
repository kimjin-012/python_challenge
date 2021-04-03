from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Shows

# Create your views here.
def index(request):
    return redirect('/shows/new')

def new(request):
    context = {
        'objects':Shows.objects.all()
    }
    return render(request, 'index.html', context)

def shows(request):
    context = {
        'objects':Shows.objects.all()
    }
    return render(request, 'shows.html', context)

def add(request):
    
    error = Shows.objects.validator(request.POST)
    
    if len(error) > 0:
        for key, val in error.items():
            messages.error(request, val)
        return redirect('/shows/new')
    
    title = request.POST['title']
    network = request.POST['network']
    date = request.POST['release']
    desc = request.POST['desc']
    
    newshow = Shows.objects.create(title=title, network=network, date=date, desc=desc)
    return redirect(f'/shows/{newshow.id}')

def edit(request, num):
    context = {
        'objects':Shows.objects.get(id=num),
    }
    return render(request, 'edit.html', context)

def display(request, num):
    context = {
        'objects':Shows.objects.get(id=num),
    }
    return render(request, 'display.html', context)

def editshow(request):
    
    error = Shows.objects.validator(request.POST)
    
    if len(error) > 0:
        for key, val in error.items():
            messages.error(request, val)
        return redirect('/shows/new')
    
    title = request.POST['title']
    network = request.POST['network']
    date = request.POST['release']
    desc = request.POST['desc']
    showid = request.POST['showid']
    
    showedit = Shows.objects.get(id=int(showid))
    showedit.title = title
    showedit.network = network
    showedit.date = date
    showedit.desc = desc
    showedit.save()
    
    return redirect(f'/shows/{showid}')

def destroy(request, num):
    show_delete = Shows.objects.get(id=num)
    show_delete.delete()
    
    return redirect('/shows')