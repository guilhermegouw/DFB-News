import pytest

from django.urls import reverse


def test_home_page_correct_location(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_name(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200


def test_home_page_uses_correct_template(client):
    response = client.get(reverse("home"))
    templates_found = [template.name for template in response.templates]
    assert "home.html" in templates_found

def test_home_page_template_content(client):
    response = client.get(reverse("home"))
    assert "<title>Home</title>" in response.content.decode()
