from django.urls import reverse
import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = reverse("product:category-list")

    def test_category_list(self, category_factory, api_client):
        # Arrange
        category_factory.create_batch(5)
        # Act
        response = api_client.get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5

    def test_category_retrieve(self, category_factory, api_client):
        # Arrange
        category = category_factory.create_batch(5)
        # Act
        response = api_client.get(
            reverse("product:category-detail", kwargs={"pk": category[0].pk})
        )
        # Assert
        assert response.status_code == 200
        assert json.loads(response.content)["name"] == category[0].name


class TestBrandEndpoints:
    endpoint = reverse("product:brand-list")

    def test_brand_list(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(5)
        # Act
        response = api_client.get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5


class TestProductEndpoints:
    endpoint = reverse("product:product-list")

    def test_product_list(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(5)
        # Act
        response = api_client.get(self.endpoint)
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
