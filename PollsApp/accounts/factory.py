import factory

from accounts.models import User

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    photo = factory.django.ImageField(color='green')


    class Meta:
        model = User