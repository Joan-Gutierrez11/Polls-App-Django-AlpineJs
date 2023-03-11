import factory
import factory.fuzzy
import datetime
import pytz

from accounts.models import User

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    photo = factory.django.ImageField(color='green')
    date_joined = factory.fuzzy.FuzzyDateTime(datetime.datetime(2020, 1, 1, tzinfo=pytz.UTC))

    class Meta:
        model = User