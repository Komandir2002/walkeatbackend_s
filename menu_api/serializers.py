from rest_framework import serializers
from .models import Fit, Category, Cart,Order


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


class FitSerializer(serializers.ModelSerializer):
    category = CategoriesSerializers(many=True)

    class Meta:
        model = Fit
        fields = "__all__"
        exta_kwargs = {"price": {"read_only": True}}


class FitMenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=35, read_only=True)
    price = serializers.CharField(max_length=255, read_only=True)
    kcal = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Fit
        fields = ["title", "price", "kcal"]


class CartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=35, read_only=True)
    get_name_food = serializers.CharField(max_length=250, read_only=True)
    total_price = serializers.CharField(max_length=255)

    class Meta:
        model = Cart
        fields = ["user", "get_name_food", "total_price", "updated_at", "created_at"]

class OrderSerializer(serializers.ModelSerializer):
    # cart_user_id = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = Order
        fields = "__all__"

