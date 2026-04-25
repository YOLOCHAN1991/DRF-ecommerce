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
    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.name)


class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="attribute_value"
    )

    def __str__(self):
        return self.attribute_value

 

class ProductLine(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    sku = models.CharField(max_length=100, null=True, blank=True)
    stock_qty = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line"
    )
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field="product", blank=True)
    attribute_value = models.ManyToManyField(
        AttributeValue, through="ProductLineAttributeValue", related_name="product_line_attribute_value"
    )
    objects = ActiveQueryset().as_manager()

    def clean(self, exclude: Collection[str] | None = ...) -> None:
        qs = ProductLine.objects.filter(product=self.product).exclude(pk=self.pk)
        for obj in qs:
            if obj.sku == self.sku:
                raise ValidationError("SKU must be unique per product")
            if obj.order == self.order:
                raise ValidationError("Order must be unique per product")
        # qs = ProductLine.objects.filter(product=self.product)
        # for obj in qs:
        #     if self.id != obj.id and self.order == obj.order:
        #         raise ValidationError("Duplicate value.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLine, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.sku)


class ProductLineAttributeValue(models.Model):
    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.CASCADE,
        related_name="product_attribute_value_av",
    )
    product_line = models.ForeignKey(
        ProductLine, on_delete=models.CASCADE, related_name="product_attribute_value_pl"
    )

    class Meta:
        unique_together = ("attribute_value", "product_line")


class ProductImage(models.Model):
    alt_text = models.CharField(max_length=100)
    url_image = models.ImageField(upload_to="products", default="test.jpg")
    productline = models.ForeignKey(
        ProductLine, on_delete=models.PROTECT, related_name="product_image"
    )
    order = OrderField(unique_for_field="productline", blank=True)

    def clean(self, exclude: Collection[str] | None = ...) -> None:
        qs = ProductImage.objects.filter(productline=self.productline).exclude(
            pk=self.pk
        )
        for obj in qs:
            # if obj.sku == self.sku:
            #     raise ValidationError("SKU must be unique per product")
            if obj.order == self.order:
                raise ValidationError("Order must be unique per product")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url_image)
