from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

from .forms import loginForm

def list(request):
#    todoform = TodoForm()
    return render(request,'api/index.html')

def login_view(request):
#    login_form = loginForm()
    return render(request,'api/login_view.html')
