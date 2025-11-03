from django.shortcuts import get_object_or_404
from django.shortcuts import render

from lettings.models import Letting


def index(request):
    """
    Display the list of all lettings.

    @param request: The HTTP request object
    @type request: django.http.HttpRequest
    @return: Rendered HTML page with all lettings
    @rtype: django.http.HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    """
    Display the details of a specific letting.

    @param request: The HTTP request object
    @type request: django.http.HttpRequest
    @param letting_id: Unique ID of the letting
    @type letting_id: int
    @return: Rendered HTML page with letting details
    @rtype: django.http.HttpResponse
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
