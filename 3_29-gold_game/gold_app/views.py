from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
import random

# Create your views here.
def index(request):
    if 'current' not in request.session:
        request.session['current'] = 0
    else:
        request.session['current'] += request.session['income']
    if 'action' not in request.session:
        request.session['action'] = []
    if 'gain' not in request.session:
        request.session['gain'] = True
    
    return render(request, 'index.html')

def process(request):
    context = strftime('%Y/%m/%d %H:%M %p', localtime())
    if request.POST['which_work'] == 'farm':
        request.session['income'] = random.randint(10,20)
        request.session['gain'] = True
        much = request.session['income']
        request.session['action'].append(f'Earned {much} golds from the farm! ({context}) \n ')
    elif request.POST['which_work'] == 'cave':
        request.session['income'] = random.randint(5,10)
        request.session['gain'] = True
        much = request.session['income']
        request.session['action'].append(f'Earned {much} golds from the cave! ({context}) \n ')
    elif request.POST['which_work'] == 'house':
        request.session['income'] = random.randint(2,5)
        request.session['gain'] = True
        much = request.session['income']
        request.session['action'].append(f'Earned {much} golds from the house! ({context}) \n ')
    elif request.POST['which_work'] == 'casino':
        request.session['income'] = random.randint(-50,50)
        much = request.session['income']
        if much > 0:
            request.session['gain'] = True
            request.session['action'].append(f'Entered a casino and gained {much} gold! OMG! ({context}) \n ')
        elif much == 0:
            request.session['gain'] = True
            request.session['action'].append(f'Waste of time... ({context})')
        elif much < 0:
            request.session['gain'] = False
            request.session['action'].append(f'Entered a casino and lost {much} golds... Idiot ({context}) \n ')
    return redirect('/')

def delete(request):
    del request.session['current']
    del request.session['action']
    return redirect('/')