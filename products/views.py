from django.shortcuts import render
from.models import product

# Create your views here.

def product_list(request):
    products=product.objects.all()
    return render(request,"products/home.html",{"products":products})


def product_details(request,id):
    details=product.objects.get(id=id)
    return render(request,"products/details.html",{"details":details})



