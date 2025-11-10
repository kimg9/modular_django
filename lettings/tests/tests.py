from django.test import TestCase
from django.urls import resolve
from django.urls import reverse

from lettings import views

from ..models import Letting
from .letting_factory import AddressFactory
from .letting_factory import LettingFactory


class LettingTest(TestCase):
    def setUp(self):
        super().setUp()
        self.address_number = "1"
        self.address_street = "Main Street"
        self.address = AddressFactory(number=self.address_number, street=self.address_street)
        self.letting = LettingFactory(title="Charming Loft", address=self.address)

    def test_letting_creation(self):
        self.assertEqual(self.letting.title, "Charming Loft")
        self.assertIsNotNone(self.letting.address)
        self.assertEqual(str(self.letting), "Charming Loft")

    def test_address_creation(self):
        self.assertEqual(str(self.letting.address), f"{self.address_number} {self.address_street}")

    def test_lettings_index_url_resolves(self):
        url = reverse("lettings:index")
        assert resolve(url).func == views.index

    def test_letting_detail_url_resolves(self):
        url = reverse("lettings:letting", args=[1])
        assert resolve(url).func == views.letting

    def test_lettings_detail_view(self):
        url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(url)
        code = response.status_code
        self.assertEqual(code, 200)
        self.assertTemplateUsed(response, 'letting.html')
        self.assertEqual(response.context["title"], self.letting.title)
        self.assertEqual(response.context["address"], self.letting.address)

    def test_lettings_detail_view_unknown(self):
        url = reverse("lettings:letting", args=[142])
        response = self.client.get(url)
        code = response.status_code
        self.assertEqual(code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_letting_list_view(self):
        LettingFactory(title="Amazing cottage")
        lettings = Letting.objects.all()
        self.assertEqual(len(lettings), 2)

        url = reverse("lettings:index")
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'lettings_index.html')
        self.assertEqual(list(response.context["lettings_list"]), list(lettings))
