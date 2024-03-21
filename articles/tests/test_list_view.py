import pytest

from django.urls import reverse


def test_list_article_exists_at_desired_location(client, db):
    response = client.get("/articles/")
    assert response.status_code == 200


def test_list_article_view_name(client, db):
    response = client.get(reverse("article_list"))
    assert response.status_code == 200


def test_list_article_uses_correct_template(client, db):
    response = client.get(reverse("article_list"))
    templates_found = [template.name for template in response.templates]
    assert "article_list.html" in templates_found
