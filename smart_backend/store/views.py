from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartSerializer



class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        category = self.request.query_params.get('category')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        search = self.request.query_params.get('search')
        sort = self.request.query_params.get('sort')

        if category:
            queryset = queryset.filter(category=category)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )

        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'name_asc':
            queryset = queryset.order_by('name')
        elif sort == 'name_desc':
            queryset = queryset.order_by('-name')

        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(generics.GenericAPIView):
    serializer_class = CartSerializer

    def get_cart(self, session_id):
        cart, _ = Cart.objects.get_or_create(session_id=session_id)
        return cart

    def get(self, request):
        session_id = request.query_params.get('session_id', 'guest')
        cart = self.get_cart(session_id)
        return Response(CartSerializer(cart).data)


class AddToCartView(generics.GenericAPIView):

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        session_id = request.data.get('session_id', 'guest')

        cart, _ = Cart.objects.get_or_create(session_id=session_id)
        product = Product.objects.get(id=product_id)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity

        item.save()

        return Response({"message": "Added to cart"}, status=201)


class UpdateCartItemView(generics.GenericAPIView):

    def put(self, request, pk):
        item = CartItem.objects.get(id=pk)
        item.quantity = request.data.get('quantity', item.quantity)
        item.save()

        return Response({"message": "Updated"})


class DeleteCartItemView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
