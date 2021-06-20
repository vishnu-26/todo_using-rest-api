from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

#from .forms import TodoForm

def list(request):
#    todoform = TodoForm()
    return render(request,'api/index.html')
