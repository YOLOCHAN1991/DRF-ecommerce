import factory

from apps.product.models import Category, Brand, Product, ProductImage, ProductLine


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category_{n}")
    slug = factory.Faker("slug")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker("name")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("name")
    slug = factory.Faker("slug")
    description = factory.Faker("text")
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_active = True


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=2,
    )
    sku = factory.Faker("pystr", min_chars=5, max_chars=10)
    stock_qty = factory.Faker("pyint", min_value=0, max_value=100)
    product = factory.SubFactory(ProductFactory)
    is_active = True


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    alt_text = factory.Faker("text", max_nb_chars=100)
    url_image = factory.django.ImageField()
    productline = factory.SubFactory(ProductLineFactory)
