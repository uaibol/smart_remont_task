from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),

    path('cart/', CartView.as_view()),
    path('cart/add/', AddToCartView.as_view()),
    path('cart/<int:pk>/', UpdateCartItemView.as_view()),
    path('cart/<int:pk>/delete/', DeleteCartItemView.as_view()),
]