from django.core.exceptions import ValidationError
from collections.abc import Collection
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField

# Create your models here.


class ActiveQueryset(models.QuerySet):
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_active=True)
    def isactive(self):
        return self.filter(is_active=True)


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
    )
    objects = ActiveQueryset.as_manager()

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset().as_manager()

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    sku = models.CharField(max_length=100, null=True, blank=True)
    stock_qty = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line"
    )
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field="product", blank=True)
    objects = ActiveQueryset().as_manager()

    def clean(self, exclude: Collection[str] | None = ...) -> None:
        qs = ProductLine.objects.filter(product=self.product).exclude(pk=self.pk)
        for obj in qs:
            if obj.sku == self.sku:
                raise ValidationError("SKU must be unique per product")
            if obj.order == self.order:
                raise ValidationError("Order must be unique per product")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.sku)
