from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/sign_in')
def home(request):

    return render(request, 'customer/home.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')

    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                message = "invalid username and password"
        else:
            message = "username and password reqired"

    context = {
        'message':message
    }


    return render(request, 'customer/signin.html', context)