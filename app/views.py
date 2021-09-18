from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models 
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')