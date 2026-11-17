from django.shortcuts import render , redirect
from carts.models import cart
from .models import Orders

# Create your views here.

def checkout(request):
    cart_item=cart.objects.filter(user=request.user)
    total=sum(item.product.price * item.quantity for item in cart_item)+3000

    if request.method=="POST":
        Orders.objects.create(
            user=request.user,
            total_price=total,
        )
        cart_item.delete()
        return redirect("/carts/cart")
    return render(request,"orders/checkout.html",{"total":total})


def order(request):
    orders=Orders.objects.filter(user=request.user)
    return render(request,"orders/order.html",{"orders":orders})

