from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors
# Create your views here.
def index(request):
    context = {
        'books_info':Books.objects.all()
    }
    return render(request, 'index.html', context)

def books(request, number):
    # return HttpResponse(f"{number}")
    context = {
        'info':Books.objects.get(id=int(number)),
        'author_info':Authors.objects.all(),
    }
    return render(request, 'books.html', context)

def addbook(request):
    title = request.POST['title']
    desc = request.POST['desc']
    
    Books.objects.create(title=title, desc=desc)
    return redirect('/')

def connectbook(request):
    authorid = request.POST['authorid']
    bookid = request.POST['bookid']
    
    ath = Authors.objects.get(id=int(authorid))
    bk = Books.objects.get(id=int(bookid))
    
    ath.book.add(bk)
    return redirect(f'books/{bookid}')

# ----- authors -----
def authors(request):
    context = {
        'person_info':Authors.objects.all()
    }
    return render(request, 'authors.html', context)

def addauthors(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    notes = request.POST['notes']
    
    Authors.objects.create(first_name=fname, last_name=lname, notes=notes)
    return redirect('/authors')

def authorinfo(request, number):
    context = {
        'info':Authors.objects.get(id=int(number)),
        'book_info':Books.objects.all(),
    }
    return render(request, 'authorsinfo.html', context)

def connectauthor(request):
    authorid = request.POST['authorid']
    bookid = request.POST['bookid']
    
    ath = Authors.objects.get(id=int(authorid))
    bk = Books.objects.get(id=int(bookid))
    
    ath.book.add(bk)
    return redirect(f'authors/{authorid}')