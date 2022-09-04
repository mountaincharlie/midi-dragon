from django.shortcuts import render

def handler404(request, exception):
    """ Django's handler function for custom 404 pages """
    return render(request, "errors/404.html", status=404)
