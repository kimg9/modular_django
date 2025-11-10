import random

import factory

from ..models import Address
from ..models import Letting


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    number = random.randint(1, 35)
    street = "Champs-Elysées"
    city = "Paris"
    state = "FR"
    zip_code = 75000
    country_iso_code = "FRA"


class LettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Letting

    title = factory.Sequence(lambda n: f"Letting {n}")
    address = factory.SubFactory(AddressFactory)
