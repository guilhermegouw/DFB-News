import pytest

from django.urls import reverse

from .factories import ArticleFactory
from accounts.tests.factories import CustomUserFactory


@pytest.fixture
def article(db):
    return ArticleFactory()

@pytest.fixture
def logged_in_user(client, db):
    user = CustomUserFactory()
    client.force_login(user)
    return user


def test_article_detail_exists_at_desired_location(client, db, article, logged_in_user):
    response = client.get(f"/articles/{article.pk}/")
    assert response.status_code == 200



def test_article_detail_view_name(client, db, article, logged_in_user):
    response = client.get(reverse("article_detail", kwargs={"pk": f"{article.pk}"}))
    assert response.status_code == 200
    failed = client.get(reverse("article_detail", kwargs={"pk": f"{article.pk + 1}"}))
    assert failed.status_code == 404

def test_article_detail_uses_correct_template(client, db, article, logged_in_user):
    response = client.get(reverse("article_detail", kwargs={"pk": f"{article.pk}"}))
    templates_found = [template.name for template in response.templates]
    assert "article_detail.html" in templates_found
