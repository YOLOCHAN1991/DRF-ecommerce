from rest_framework import serializers

from .models import Category, Brand, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = ("price", "sku", "stock_qty")


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "brand_name",
            "category_name",
            "product_line",
        )
