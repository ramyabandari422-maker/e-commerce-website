from django.urls import path
from products import views

urlpatterns=[
    path("",views.product_list,name="home"),
    path("details/<int:id>",views.product_details,name="pro_details"),

    
]