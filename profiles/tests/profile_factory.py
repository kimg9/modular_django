import factory

from oc_lettings_site.tests.user_factory import UserFactory
from profiles.models import Profile


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    favorite_city = "Lyon"
