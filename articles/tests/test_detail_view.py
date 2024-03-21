import pytest

from django.urls import reverse

from .factories import ArticleFactory


@pytest.fixture
def article(db):
    return ArticleFactory()


def test_article_detail_exists_at_desired_location(client, db, article):
    response = client.get(f"/articles/{article.pk}/")
    assert response.status_code == 200



def test_article_detail_view_name(client, db, article):
    response = client.get(reverse("article_detail", kwargs={"pk": f"{article.pk}"}))
    assert response.status_code == 200
    failed = client.get(reverse("article_detail", kwargs={"pk": f"{article.pk + 1}"}))
    assert failed.status_code == 404

def test_article_detail_uses_correct_template(client, db, article):
    response = client.get(reverse("article_detail", kwargs={"pk": f"{article.pk}"}))
    templates_found = [template.name for template in response.templates]
    assert "article_detail.html" in templates_found
