from django.contrib import admin

from .models import Category, Brand, Product, ProductLine


class ProductLineInline(admin.TabularInline):
    model = ProductLine
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductLine)
