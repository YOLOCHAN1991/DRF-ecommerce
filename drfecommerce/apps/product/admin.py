from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Category, Brand, Product, ProductLine, ProductImage


class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )
        print(url)
        if instance.pk:
            link = mark_safe("<a href=" + url + ">Edit</a>")
            return link
        else:
            return ""


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ["edit"]
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
