from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("category", views.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
