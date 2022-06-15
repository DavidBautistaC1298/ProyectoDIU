from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario registrado')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = { 'form' : form }
    return render(request, 'registro.html', context)

def tramitepresencial(request):
    return render(request, 'tramitepresencial.html')

def subirarchivos(request):
    return render(request, 'subirarchivos.html')

def tramitenacional(request):
    return render(request, 'tramitenacional.html')

def tramiteinternacional(request):
    return render(request, 'tramiteinternacional.html')
