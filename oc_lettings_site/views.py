from django.shortcuts import render


def index(request):
    """
    Display the home page of the OC Lettings Site.

    @param request: The HTTP request object
    @type request: django.http.HttpRequest
    @return: Rendered HTML page for the homepage
    @rtype: django.http.HttpResponse
    """
    return render(request, 'index.html')
