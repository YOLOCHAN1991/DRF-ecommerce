from django.urls import include, path
from . import views
from rest_framework import routers

app_name = "product"

router = routers.DefaultRouter()
router.register("category", views.CategoryViewSet, basename="category")
router.register("brand", views.BrandViewSet, basename="brand")
router.register("productline", views.ProductLineViewSet, basename="productline")
router.register("product", views.ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]
