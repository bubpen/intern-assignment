import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from account.models import CustomUser

@pytest.mark.django_db
class TestSignup:
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("signup")  # urls.py에 name="signup"이 있어야 함

    def test_signup_success(self):
        data = {
            "username": "testuser",
            "password": "testpass123",
            "nickname": "tester"
        }
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == 201
        assert response.data["username"] == "testuser"
        assert response.data["nickname"] == "tester"

    def test_signup_duplicate_username(self):
        # 먼저 사용자 생성
        CustomUser.objects.create_user(username="testuser", password="testpass123", nickname="tester")
        # 중복 요청
        data = {
            "username": "testuser",
            "password": "testpass123",
            "nickname": "tester"
        }
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == 400
        assert response.data["error"]["code"] == "USER_ALREADY_EXISTS"
        assert "가입된 사용자" in response.data["error"]["message"]
