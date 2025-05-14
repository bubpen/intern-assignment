import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from account.models import CustomUser

@pytest.mark.django_db
class TestLogin:
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("login")
        self.user = CustomUser.objects.create_user(username="testuser", password="testpass123", nickname="tester")

    def test_login_success(self):
        data = {
            "username": "testuser",
            "password": "testpass123"
        }
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == 200
        assert "token" in response.data

    def test_login_fail(self):
        data = {
            "username": "testuser",
            "password": "wrongpass"
        }
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == 400
        assert response.data["error"]["code"] == "INVALID_CREDENTIALS"
