
from django.urls import path
from .views_two  import  PaymentView
from .views import (
    HomeView, 
    ItemDetailView, 
    add_to_cart, 
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,

    ) 



app_name = 'shop'
urlpatterns = [

    path('',                                HomeView.as_view(),             name="home-view"),
    path('checkout/',                       CheckoutView.as_view(),         name="checkout"),
    path('product/<slug>/',                 ItemDetailView.as_view(),       name="product"),
    path('add-to-cart/<slug>/',             add_to_cart,                    name="add-to-cart"),
    path('remove-from-cart/<slug>/',         remove_from_cart,              name="remove-from-cart"),
    path('order-summary-view/',             OrderSummaryView.as_view(),     name="order-summary-view"),
    path('remove-single-item-from-cart/<slug>/',   remove_single_item_from_cart,    name="remove-item-from-cart"),
    
    # views_two
    path('payment/<payement_option>/',   PaymentView.as_view(),    name="payment"),
]
