from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        'everyone_info':User.objects.all()
    }
    return render(request, 'index.html', context)

def add(request):
    fname = request.POST['f_name']
    lname = request.POST['l_name']
    email = request.POST['e_mail']
    age = int(request.POST['a_g'])
    
    User.objects.create(first_name = fname, last_name = lname, email_address = email, age = age)
    return redirect('/')