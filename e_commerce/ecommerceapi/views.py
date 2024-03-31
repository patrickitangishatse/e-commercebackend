from .models import Product, Category, Cart, CartItems
from .serializers import ProductSerializer, CategorySerializer, CartSerializer, CartItemsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination



# Create your views here.


# All Products
class CreateProduct(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    pagination_class = PageNumberPagination

# Get Single Product and Update,Delete Product
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


# Get all Category and Create Category
class CreateCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  


# Get Single Category and Update,Delete Category
class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"


# Get all Cart and Create Cart
class CartListView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Get Single Cart and Update,Delete Cart

class CartDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "pk"

class CartItems(ListCreateAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer




# @api_view(['GET','POST'])
# def Products(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)




# @api_view(['GET','PUT','DELETE'])
# def ProductDetail(request,pk):
#     if request.method == 'GET':
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
#     if request.method=="PUT":
#         product=Product.objects.get(id=pk)
#         serializer=ProductSerializer(product,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=400)
    
#     if request.method=="DELETE":
#         product=Product.objects.get(id=pk)
#         product.delete()
#         return Response(status=204)



# @api_view(['GET','POST'])
# def Categories(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# @api_view(['GET','PUT','DELETE'])
# def CategoryDetail(request,pk):
#     if request.method == 'GET':
#         category = Category.objects.get(id=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
    
#     if request.method=="PUT":
#         category=Category.objects.get(id=pk)
#         serializer=CategorySerializer(category,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=400)
    
#     if request.method=="DELETE":
#         category=Category.objects.get(id=pk)
#         category.delete()
#         return Response(status=204)