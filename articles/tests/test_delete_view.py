import pytest

from django.urls import reverse

from .factories import ArticleFactory
from articles.models import Article


@pytest.fixture
def article(db):
    return ArticleFactory()


def test_article_delete_exists_at_desired_location(client, db, article):
    response = client.get(f"/articles/{article.pk}/delete/")
    assert response.status_code == 200
    failed = client.get(reverse("article_delete", kwargs={"pk": f"{article.pk + 1}"}))
    assert failed.status_code == 404


def test_article_delete_view_name(client, db, article):
    response = client.get(reverse("article_delete", kwargs={"pk": f"{article.pk}"}))
    assert response.status_code == 200
    failed = client.get(reverse("article_delete", kwargs={"pk": f"{article.pk + 1}"}))
    assert failed.status_code == 404


def test_delete_article_can_delete_article(client, db, article):
    response = client.delete(reverse("article_delete", kwargs={"pk": f"{article.pk}"}))
    assert response.status_code == 302
    assert Article.objects.count() == 0


def test_article_delete_uses_correct_template(client, db, article):
    response = client.get(reverse("article_delete", kwargs={"pk": f"{article.pk}"}))
    templates_found = [template.name for template in response.templates]
    assert "article_delete.html" in templates_found
