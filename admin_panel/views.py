from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):

    return render(request, 'admin_panel/home.html')

def product(request):
    message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        expire_date = request.POST.get('expire_date')
        description = request.POST.get('description')

        if name and price and stock and expire_date and description:
            if stock == 'yes':
                stock = True
            else:
                stock = False
            Product.objects.create(
                name=name,
                image=image,
                price=price,
                stock=stock,
                exprire_date=expire_date,
                description=description
            )

            message = f"Product {name} has been Added Successfuly"
        else:
            message = "all field are reqired"

    all_product = Product.objects.all()

    context = {
        'all_product': all_product,
        'message':message
    }

    return render (request, 'admin_panel/product.html',context)
