from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def tramitepresencial(request):
    return render(request, 'tramitepresencial.html')

def subirarchivos(request):
    return render(request, 'subirarchivos.html')

def tramitenacional(request):
    return render(request, 'tramitenacional.html')

def tramiteinternacional(request):
    return render(request, 'tramiteinternacional.html')
