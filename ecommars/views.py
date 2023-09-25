from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'ecommars/home.html')

def product(request):

    return render(request,'ecommars/product.html')