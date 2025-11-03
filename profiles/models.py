from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Model representing a user profile.

    @cvar user: One-to-one relationship with Django User model
    @cvar favorite_city: Optional favorite city of the user (max 64 chars)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return the username associated with the profile.

        @return: Username of the profile
        @rtype: str
        """
        return self.user.username

    class Meta:
        db_table = 'oc_lettings_site_profile'
