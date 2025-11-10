from django.test import TestCase
from django.urls import reverse


class HomePageViewTest(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
