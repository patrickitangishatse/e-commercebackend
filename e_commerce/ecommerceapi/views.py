from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema

# Swagger decorations for api_products
@swagger_auto_schema(
    method='get', 
    operation_description='Get a list of products',
    responses={200: ProductSerializer(many=True)}
)
@swagger_auto_schema(
    method='post', 
    operation_description='Create a new product',
    request_body=ProductSerializer,
    responses={201: ProductSerializer()}
)
@api_view(['GET', 'POST'])
def api_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Swagger decorations for api_product
@swagger_auto_schema(
    method='get', 
    operation_description='Get details of a product',
    responses={200: ProductSerializer()}
)
@swagger_auto_schema(
    method='put', 
    operation_description='Update details of a product',
    request_body=ProductSerializer,
    responses={200: ProductSerializer()}
)
@swagger_auto_schema(
    method='delete', 
    operation_description='Delete a product',
    responses={204: 'No Content'}
)
@api_view(['GET', 'PUT', 'DELETE'])
def api_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "GET":
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Other views with Swagger decorations can be added here

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_to_cart(request):
    # Add your logic to add a product to the user's cart
    return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def checkout(request):
    # Add your logic for the checkout process
    return Response({'message': 'Checkout successful'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def make_payment(request):
    # Add your logic for processing payment
    return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)
