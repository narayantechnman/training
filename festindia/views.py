from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from service.models import Service
from news.models import News

def homepage(request):
    newsdata=News.objects.all()
    servicesData=Service.objects.all().order_by('-name')

    data={
        'services':servicesData,
        'newsData':newsdata
    }

    return render(request, 'index.html',data)

def news(request):
    newsdata=News.objects.get()
    data={
        'newsData':newsdata  
    }
    return render(request, 'news.html',data)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def product(request):
    return render(request, 'product.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use auth_login instead of login
                return redirect('profile')  # Redirect to profile page after successful login
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'username': request.user.username})
    else:
        return redirect('login')