from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def register(request):
    
    error = Users.objects.validator(request.POST)
    
    if len(error) > 0:
        for key, val in error.items():
            messages.error(request, val)
        return redirect('/')
    
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    pword = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    email = request.POST['email']
    
    newuser = Login.objects.create(first_name = fname, last_name=lname, email=email, password=pword)
    
    request.session['fname'] = fname
    request.session['lname'] = lname
    request.session['email'] = email
    request.session['id'] = newuser.id
    
    return redirect('/success')

def login(request):
    error = Users.objects.login_vali(request.POST)
    
    if len(error) > 0:
        for key, val in error.items():
            messages.error(request, val)
        return redirect('/')
    
    user = Users.objects.filter(email = request.POST['email'])
    logged_user = user[0]
    request.session['id'] = logged_user.id
    request.session['fname'] = logged_user.first_name
    
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')