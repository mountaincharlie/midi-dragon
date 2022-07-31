from django.shortcuts import render


def index(request):
    """ View for returning the index.html """

    return render(request, 'home/index.html')
