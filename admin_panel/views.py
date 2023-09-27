from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):

    return render(request, 'admin_panel/home.html')

def product(request):

    all_product = Product.objects.all()

    context = {
        'all_product': all_product
    }

    return render (request, 'admin_panel/product.html',context)
