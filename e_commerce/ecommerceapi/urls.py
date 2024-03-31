from django.urls import path
from .views import CreateProduct, ProductDetail,CreateCategory,CategoryDetail, CartListView, CartItems,CartDetail

urlpatterns = [
    path('products/', CreateProduct.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('categories/', CreateCategory.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartDetail.as_view(), name='cart-detail'),
    path('cartitems/', CartItems.as_view(), name='cartitems-list')
]