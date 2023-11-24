from django.shortcuts import render

# Create your views here.
def siri(request):
    return render(request,'siri.html')

def niki(request):
    return render(request,'niki.html')

def siri2(request):
    return render(request,'siri2.html')

def niki2(request):
    return render(request,'niki2.html')

def siri3(request):
    return render(request,'siri3.html')