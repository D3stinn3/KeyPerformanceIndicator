from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'Backend/base.html', context)

def calender(request):
    context = {}
    return render(request, 'Backend/calendar.html', context)

def kpibreakdown(request):
    context = {}
    return render(request, 'Backend/personal.html', context)