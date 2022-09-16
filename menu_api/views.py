from django.shortcuts import render
from .serializers import (
    FitSerializer,
    FitMenuSerializer,
    CategoriesSerializers,
    CartSerializer,
    OrderSerializer,

)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Fit, Category, Cart, Order
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .pagination import FitPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView

class FitViewSet(ModelViewSet):
    pagination_class = FitPagination
    permission_classes = [IsAdminUser]
    queryset = Fit.objects.all()
    serializer_class = FitSerializer
    authentication_classes = [
        JWTAuthentication,
    ]


class FitListApiView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = FitSerializer
    # pagination_class = FitPagination
    queryset = Fit.objects.all()


class FitMenuView(ListAPIView):
    # pagination_class = FitPagination

    serializer_class = FitMenuSerializer
    queryset = Fit.objects.all()
    authentication_classes = [
        JWTAuthentication,
    ]


class CategoryView(ListAPIView):

    serializer_class = CategoriesSerializers
    queryset = Category.objects.all()
    authentication_classes = [
        JWTAuthentication,
    ]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()

    serializer_class = CartSerializer
    authentication_classes = JWTAuthentication

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = JWTAuthentication
