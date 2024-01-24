from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# Get all products and create product. 
@api_view(['GET',"POST"])
def api_products(request):
        if request.method=="GET":
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        
        if request.method=="POST":
            serializer=ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
 
# Get product by Id
@api_view(['GET','PUT','DELETE'])
def api_product(request,pk):
        product = get_object_or_404(Product, id=pk)
        if request.method=="GET":
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data)
        
# Update a product using its ID
        if request.method=="PUT":
            serializer = ProductSerializer(product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
# Delete a product using its ID
        if request.method=="DELETE":
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
