from django.shortcuts import render


def view_tracklist(request):
    """ View to return the tracklist page """

    return render(request, 'tracklist/tracklist.html')

# class TracklistView(View):
#     """
#     Class based view inheriting Django's View
#     Contains the get method for displaying the songs that the user has
#     in their tracklist
#     """
#     def get(self, request, *args, **kwargs):
