from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import (
    api_products,
    api_product,
    register_user,
    user_login,
    user_logout,
    add_to_cart,
    checkout,
    make_payment,
)

# Define app_name in your app's urls.py
app_name = 'your_app'

# API URLs
api_patterns = [
    path("products/", api_products, name="api-products"),
    path("products/<str:pk>", api_product, name="api_product"),
    path("register/", register_user, name="register_user"),
    path("login/", user_login, name="user_login"),
    path("logout/", user_logout, name="user_logout"),
    path("add_to_cart/", add_to_cart, name="add_to_cart"),
    path("checkout/", checkout, name="checkout"),
    path("make_payment/", make_payment, name="make_payment"),
]

# Swagger and ReDoc URLs
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_patterns, 'your_app'), namespace='your_app')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
