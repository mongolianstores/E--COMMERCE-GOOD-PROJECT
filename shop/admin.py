from django.contrib import admin

from .models import OrderItem, Order, Item, Payment



admin.site.register(OrderItem) 
admin.site.register(Order) 
admin.site.register( Item) 
admin.site.register( Payment) 
