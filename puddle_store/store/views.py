from django.shortcuts import render
from items.models import Category,Product
# Create your views here.
def home(request):
    product=Product.objects.all()
    categorie=Category.objects.all()
    context={
        'products':product,
        'categories':categorie
    }
    return render(request,'pages/home.html',context)

def item(request):
    product=Product.objects.all()
    categorie=Category.objects.all()
    context={
        'products':product,
        'categories':categorie
    }
    return render(request,'pages/category.html',context)