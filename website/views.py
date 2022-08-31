from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get( username = username)
        except:
            return redirect('home')
            
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('index')
    context = {'page' : page}   
    return render(request, 'login_registration.html', context)

def registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            login(request,user)
            redirect('index')
        else:
            return HttpResponse('form not valid')
    context = {'form' : form}
    return render(request , 'login_registration.html', context)

@login_required(login_url='home')
def index(request):
    return render(request,'index.html')

