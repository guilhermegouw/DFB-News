import factory

from django.contrib.auth import get_user_model

from ..models import CustomUser


User = get_user_model()


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    age = factory.Faker("random_int", min=0, max=100)
