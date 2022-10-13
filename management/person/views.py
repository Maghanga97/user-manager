from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from .models import Person

# Create your views here.

def index(request):
    user = None
    try:
        user = request.user
        user = Person.objects.get(username=user)
    except:
        pass
    for n in range(10):
        print(n)    
        return render(request, 'person/index.html', {'user': n})
        


def register(request):
    MSG = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            MSG = 'A new user has been created'
            return redirect('/login/')
        
        else:
            MSG = 'An error occurred during signup'
    else:
        form = SignupForm()
    return render(request, 'person/register.html', {'message': MSG, 'form': form})


def login_view(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('pwd')
        valid_user = authenticate(username=user, password=password)
        if valid_user:
            login(request, valid_user)
            print('User logged in successfully:', request.user)
            return redirect('/')

    return render(request, 'person/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('/login/')


def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_pwd')
        user = Person.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        
    return render(request, 'person/reset-password.html')