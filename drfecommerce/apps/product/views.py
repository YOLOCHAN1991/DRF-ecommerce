from rest_framework.response import Response

# from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics, viewsets
from drf_spectacular.utils import extend_schema

from .models import Product, Brand, Category
from .serializers import (  # noqa
    ProductSerializer,
    BrandSerializer,
    CategorySerializer,
    CategoryNameSerializer,
)


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses={200: CategoryNameSerializer(many=True)})
    def list(self, request):
        serializer = CategoryNameSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategoryNameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        category = generics.get_object_or_404(self.queryset, pk=pk)
        serializer = CategoryNameSerializer(category)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()

    @extend_schema(responses={200: BrandSerializer(many=True)})
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        brand = generics.get_object_or_404(self.queryset, pk=pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    @extend_schema(responses={200: ProductSerializer(many=True)})
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = generics.get_object_or_404(self.queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
