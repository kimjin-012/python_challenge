from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'guess' not in request.session:
        request.session['guess'] = random.randint(1,100)
    if 'correct' not in request.session:
        request.session['correct'] = False
    if 'counts' in request.session:
        request.session['counts'] += 1
    else:
        request.session['counts'] = 0
    if 'tries' not in request.session:
        request.session['tries'] = 5
    else:
        request.session['tries'] -= 1
    return render(request, 'index.html')

def check(request):
    checknum = request.POST['answer']
    if request.session['guess'] == int(checknum):
        request.session['correct'] = True
    elif request.session['guess'] < int(checknum):
        request.session['high'] = True
    elif request.session['guess'] > int(checknum):
        request.session['high'] = False
    return redirect('/')

def reset(request):
    del request.session['guess']
    del request.session['correct']
    del request.session['counts']
    del request.session['high']
    del request.session['tries']
    return redirect('/')