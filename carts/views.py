from django.shortcuts import render,redirect
from products.models import product
from .models import cart
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_to_cart(request,id):
    products=product.objects.get(id=id)
    cart_item,created=cart.objects.get_or_create(
        user=request.user,
        product=products
    )

    if not created:
        cart_item.quantity+=1
    cart_item.save()
    return redirect("/")

@login_required
def cart_view(request):
    items=cart.objects.filter(user=request.user)
    total=sum(i.product.price * i.quantity  for i in items)+3000
    return render(request,"carts/cart.html",{"items":items,"total":total})

@login_required
def cart_delete(request,id):
    cart.objects.get(id=id).delete()
    return redirect("/carts/cart")
