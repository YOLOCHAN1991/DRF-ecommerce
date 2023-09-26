from django.db import connection
from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework.decorators import action

# from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics, viewsets
from drf_spectacular.utils import extend_schema

from .models import Product, Brand, Category, ProductLine
from .serializers import (  # noqa
    ProductSerializer,
    BrandSerializer,
    CategorySerializer,
    ProductLineSerializer,
)


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(responses={200: CategorySerializer(many=True)})
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        category = generics.get_object_or_404(self.queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

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


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().isactive()
    serializer_class = ProductSerializer
    lookup_field = "slug"

    def list(self, request):
        """List all products"""
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        """Retrieve a product"""
        # product = generics.get_object_or_404(self.queryset, slug=slug)
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug)
            .select_related("category", "brand")
            .prefetch_related(Prefetch("product_line"))
            .prefetch_related(Prefetch("product_line__product_image")),
            many=True,
        )

        data = Response(serializer.data)
        print(len(connection.queries))
        return data

    @action(
        methods=["GET"],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)",
        url_name="all-by-category",
    )
    def list_product_by_category(self, request, slug=None):
        """List all products by category"""
        serializer = ProductSerializer(
            self.queryset.filter(category__slug=slug), many=True
        )
        return Response(serializer.data)

    def create(self, request):
        """Create a new product"""
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductLineViewSet(viewsets.ModelViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer
