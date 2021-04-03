from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'counts' in request.session:
        request.session['counts'] += 1
    else:
        request.session['counts'] = 0
    
    if 'visit' in request.session:
        request.session['visit'] += 1
    else:
        request.session['visit'] = 0
    
    return render(request, 'index.html')

def delete(request):
    del request.session['counts']
    return redirect('/')

def plus(request):
    request.session['counts'] += 1
    return redirect('/')

def incre(request):
    add_much = request.POST['add']
    request.session['counts'] += (int(add_much) - 1)
    return redirect('/')
#Post.objects.filter(pk=post.pk).update(views=F('views') + 1)
# from django.shortcuts import F
# post = Post.objects.get(pk=pk)
#     post.visit_num = F('visit_num') + 1
#     post.save()