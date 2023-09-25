from django.core.exceptions import ValidationError
import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str(self, category_factory):
        # Arrange
        name = category_factory(name="fsffs")
        # Act
        result = str(name)
        # Assert
        assert result == "fsffs"


class TestBrandModel:
    def test_str(self, brand_factory):
        # Arrange
        name = brand_factory(name="sdfdg")
        # Act
        result = str(name)
        # Assert
        assert result == "sdfdg"


class TestProductModel:
    def test_str(self, product_factory):
        # Arrange
        name = product_factory(name="prueba1")
        print(name)
        # Act
        result = str(name)
        # Assert
        assert result == "prueba1"


class TestProductLineModel:
    def test_str(self, product_line_factory):
        # Arrange
        name = product_line_factory(sku="prueba2")
        # Act
        result = str(name)
        # Assert
        assert result == "prueba2"

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        # Arrange
        product = product_factory()
        product_line_factory(product=product, order=1)
        product_line_factory(product=product, order=2)

        # Act
        with pytest.raises(ValidationError):
            product_line_factory(product=product, order=1).clean()
            
