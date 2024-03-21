from django.urls import reverse
from django.contrib.auth import get_user_model

from articles.models import Article

from accounts.tests.factories import CustomUserFactory
from articles.tests.factories import ArticleFactory


User = get_user_model()

def test_article_create_exists_at_desired_location(client, db):
    response = client.get(f"/articles/new/")
    assert response.status_code == 200


def test_article_create_view_name(client, db):
    response = client.get(reverse("article_create"))
    assert response.status_code == 200


def test_create_article_can_create_article(client, db):
    articles_count = Article.objects.count()
    author = CustomUserFactory()
    response = client.post(
        reverse("article_create"),
        {
            "title": "test title",
            "body": "test body",
            "author": author.id,
        },
    )
    assert response.status_code == 302
    assert Article.objects.count() == articles_count + 1


def test_article_create_uses_correct_template(client, db):
    response = client.get(reverse("article_create"))
    templates_found = [template.name for template in response.templates]
    assert "article_create.html" in templates_found
