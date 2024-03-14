import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model


def test_signup_url_exists_at_desired_location(client):
    response = client.get("/accounts/signup/")
    assert response.status_code == 200


def test_signup_view_name(client):
    response = client.get(reverse("signup"))
    assert response.status_code == 200


def test_signup_form(client, db):
    response = client.post(
        reverse("signup"),
        {
            "username": "test",
            "email": "pXG5f@example.com",
            "age": 20,
            "password1": "testpassword",
            "password2": "testpassword",
        },
    )
    assert response.status_code == 302
    assert get_user_model().objects.count() == 1
    assert get_user_model().objects.get().username == "test"
    assert get_user_model().objects.get().email == "pXG5f@example.com"
    assert get_user_model().objects.get().age == 20
