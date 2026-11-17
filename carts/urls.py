from django.urls import path
from carts import views

urlpatterns=[
    path("add_to_cart/<int:id>",views.add_to_cart,name="add_to_cart"),
    path("cart",views.cart_view,name="cart"),
    path("cart/<int:id>",views.cart_delete,name="cart_delete"),
    
]