from rest_framework import serializers

from .models import Product, Brand, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
