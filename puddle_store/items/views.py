from .models import Category,Product
from django.shortcuts import render,get_object_or_404


def detail(request,slug):
    item=get_object_or_404(Product,slug=slug)
    
    return render(request,'pages/detail.html',{"item":item})