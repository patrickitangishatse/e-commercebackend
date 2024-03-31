from django.contrib import admin
from .models import Category, Product, Cart, CartItems

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItems)
