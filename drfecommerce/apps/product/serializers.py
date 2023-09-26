from rest_framework import serializers

from .models import Category, Brand, Product, ProductImage, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("id", "productline")


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = ("price", "sku", "stock_qty", "product_image")


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
