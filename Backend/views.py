from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreate
from .models import User

# Create your views here.
def index(request):
    context = {}
    return render(request, 'Backend/base.html', context)

def calender(request):
    context = {}
    return render(request, 'Backend/calendar.html', context)

def kpibreakdown(request):
    context = {}
    return render(request, 'Backend/kpi.html', context)

def loginpage_(request):
    if request.method == "POST":
        if 'email' in request.POST:
            
            username = authenticate(
                email=request.POST['email'],
                password=request.POST['password'] 
            )
        
            if username is not None:
                login(request, username)
                return redirect('home')
        
    context = {}
    return render(request, 'Backend/login.html', context)
    
def logoutpage_(request):
    context = {}
    return redirect('home')


def signinpage_(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
    
def landingpage_(request):
    context = {}
    return render(request, 'Backend/index.html', context)


