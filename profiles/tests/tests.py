from django.test import TestCase
from django.urls import resolve
from django.urls import reverse

from oc_lettings_site.tests.user_factory import UserFactory
from profiles import views

from ..models import Profile
from .profile_factory import ProfileFactory


class ProfileTest(TestCase):
    def setUp(self):
        super().setUp()
        self.user = UserFactory(first_name="Jean-Claude")
        self.profile = ProfileFactory(favorite_city="Marseille", user=self.user)

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.first_name, "Jean-Claude")
        self.assertEqual(self.profile.favorite_city, "Marseille")
        self.assertEqual(str(self.profile), self.profile.user.username)

    def test_lettings_index_url_resolves(self):
        url = reverse("profiles:index")
        assert resolve(url).func == views.index

    def test_letting_detail_url_resolves(self):
        url = reverse("profiles:profile", args=["username_test"])
        assert resolve(url).func == views.profile

    def test_profiles_detail_view(self):
        url = reverse("profiles:profile", args=[self.profile.user.username])
        response = self.client.get(url)
        code = response.status_code
        self.assertEqual(code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertEqual(response.context["profile"], self.profile)

    def test_profiles_detail_view_unknown(self):
        url = reverse("profiles:profile", args=["unknown"])
        response = self.client.get(url)
        code = response.status_code
        self.assertEqual(code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_profile_list_view(self):
        ProfileFactory(favorite_city="Paris")
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles), 2)

        url = reverse("profiles:index")
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'profiles_index.html')
        self.assertEqual(list(response.context["profiles_list"]), list(profiles))
