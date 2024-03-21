import pytest

from django.urls import reverse

from .factories import ArticleFactory
from accounts.tests.factories import CustomUserFactory


@pytest.fixture
def article(db):
    return ArticleFactory()


@pytest.fixture
def login_author(client, db, article):
    user = article.author
    client.force_login(user)
    return user



def test_article_edit_exists_at_desired_location(client, db, article, login_author):
    response = client.get(f"/articles/{article.pk}/edit/")
    assert response.status_code == 200
    failed = client.get(reverse("article_edit", kwargs={"pk": f"{article.pk + 1}"}))
    assert failed.status_code == 404


def test_article_edit_view_name(client, db, article, login_author):
    response = client.get(reverse("article_edit", kwargs={"pk": f"{article.pk}"}))
    assert response.status_code == 200
    failed = client.get(reverse("article_edit", kwargs={"pk": f"{article.pk + 1}"}))
    assert failed.status_code == 404


def test_edit_article_can_edit_article(client, db, article, login_author):
    response = client.post(
        reverse("article_edit", kwargs={"pk": f"{article.pk}"}),
        {
            "title": "edited title",
            "body": "edited body",
        },
    )
    assert response.status_code == 302
    article.refresh_from_db()
    assert article.title == "edited title"
    assert article.body == "edited body"


def test_article_edit_uses_correct_template(client, db, article, login_author):
    response = client.get(reverse("article_edit", kwargs={"pk": f"{article.pk}"}))
    templates_found = [template.name for template in response.templates]
    assert "article_edit.html" in templates_found
