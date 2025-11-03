from django.shortcuts import get_object_or_404
from django.shortcuts import render

from profiles.models import Profile


def index(request):
    """
    Display the list of all user profiles.

    @param request: The HTTP request object
    @type request: django.http.HttpRequest
    @return: Rendered HTML page with all profiles
    @rtype: django.http.HttpResponse
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    """
    Display the details of a specific user profile.

    @param request: The HTTP request object
    @type request: django.http.HttpRequest
    @param username: Username of the desired profile
    @type username: str
    @return: Rendered HTML page with profile details
    @rtype: django.http.HttpResponse
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
