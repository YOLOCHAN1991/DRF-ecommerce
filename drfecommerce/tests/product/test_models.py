import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str(self, category_factory):
        # Arrange
        name = category_factory(name="test")
        # Act
        result = str(name)
        # Assert
        assert result == "test"


class TestBrandModel:
    def test_str(self, brand_factory):
        # Arrange
        name = brand_factory(name="ww")
        # Act
        result = str(name)
        # Assert
        assert result == "ww"


class TestProductModel:
    def test_str(self, product_factory):
        # Arrange
        name = product_factory(name="prueba1")
        print(name)
        # Act
        result = str(name)
        # Assert
        assert result == "prueba1"
