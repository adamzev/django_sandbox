from django.shortcuts import render
from .models import Category
from django.http import HttpResponse

from .forms import PostForm

def category_dropdown(request):
    return render(request, 'quickblog.html')

def page2(request):
    return render(request, 'page2.html')
