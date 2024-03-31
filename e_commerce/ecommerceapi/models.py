from django.db import models


# Create your models here.
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"


class CartItems(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default=None)


    def __str__(self):
        return self.title


# Product Class
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    discount = models.BooleanField(default=False)
    old_price = models.FloatField(default=50.00)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    slug = models.SlugField(default=None)
    inventory = models.IntegerField(default=10)

    @property
    def price(self):
        if self.discount:
            new_price = self.old_price - ((30/100) * self.old_price)
        else:
            new_price = self.old_price
        return new_price

    def __str__(self):
        return self.name