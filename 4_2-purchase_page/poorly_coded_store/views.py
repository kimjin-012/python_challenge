from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def succeed(request):
    return render(request, "store/checkout.html")

def checkout(request):
    print('************************************')
    print(request.POST)
    print('**********************************')
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'payment' not in request.session:
        request.session['payment'] = 0
        
    quantity_from_form = int(request.POST["quantity"])
    price_from_id = int(request.POST["idnum"])
    example = Product.objects.get(id=price_from_id)
    price_from_form = float(example.price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    
    request.session['count'] += quantity_from_form
    
    request.session['payment'] += total_charge

    request.session['price_form'] = price_from_form
    
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    
    return redirect('/succeed')