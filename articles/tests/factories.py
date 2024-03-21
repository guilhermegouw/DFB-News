import factory
from ..models import Article
from django.contrib.auth import get_user_model
from accounts.tests.factories import CustomUserFactory


User = get_user_model()
class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker("text", max_nb_chars=50)
    body = factory.Faker("text")
    created_at = factory.Faker("date_time")
    author = factory.SubFactory(CustomUserFactory)
