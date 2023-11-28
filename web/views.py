from django.shortcuts import render
from .models import Furniture, Blog , Services

# Create your views here.
def index(request):
    services = Services.objects.all().order_by('?')[:3]
    furnitures = Furniture.objects.all().order_by('?')[:3]
    
    return render(request, "index.html", {'furnitures' : furnitures , 'services' : services  })

def about(request):
    return render(request, "about.html")


def blog(request):
    
    blogs = Blog.objects.all().order_by('?')
    return render(request, "blog.html", {'blogs' : blogs })


def cart(request):
    return render(request, "cart.html")


def checkout(request):
    return render(request, "checkout.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    services = Services.objects.all()
    furnitures = Furniture.objects.all()[:3]
    
    return render(request, "services.html", {'furnitures' : furnitures,'services' : services } )

def shop(request):
    
     furnitures = Furniture.objects.all().order_by('?')[:12]
     return render(request, "shop.html", {'furnitures' : furnitures })

def thankyou(request):
    return render(request, "thankyou.html")


