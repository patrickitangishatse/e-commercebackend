from rest_framework import serializers
from .models import Product,Category,Cart,CartItems


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','description','category','slug','inventory','old_price','price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title','slug']
class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['title']
class SimpleProductSerializer(serializers.ModelSerializer):
    category=SimpleCategorySerializer()
    class Meta:
        model=Product
        fields=['name','price','category']

class CartItemsSerializer(serializers.ModelSerializer):
    product=SimpleProductSerializer(many=False)
    sub_total=serializers.SerializerMethodField(method_name="total")
    class Meta:
        model=CartItems
        fields=['id','cart','product','quantity','sub_total']

    def total(self,cartitems:CartItems):
        return cartitems.quantity*cartitems.product.price




class CartSerializer(serializers.ModelSerializer):
    items=CartItemsSerializer(many=True)
    Grand_Total=serializers.SerializerMethodField(method_name="main_total")
    class Meta:
        model=Cart
        fields=['id','created_at','items','Grand_Total']
    
    def main_total(sefl,cart:Cart):
        items=cart.items.all()
        total=sum([item.quantity * item.product.price for item in items])
        return total