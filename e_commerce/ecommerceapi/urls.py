
from django.urls import path
from ecommerceapi.views import api_products
from ecommerceapi.views import api_product


urlpatterns = [
    path("products/", api_products, name="api-products"), 
    path("products/<str:pk>",api_product, name="api_product")
]