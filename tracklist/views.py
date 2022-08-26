from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from songs.models import Song


def view_tracklist(request):
    """ View to return the tracklist page """

    return render(request, 'tracklist/tracklist.html')


class AddToTracklist(View):
    """
    Class based view inheriting Django's View
    Contains the post
    """
    def post(self, request, *args, **kwargs):
        """
        View to add a song to the tracklist and redirect to the
        same song_details url or song search results
        """

        # getting the song by its pk inorder to include its name in messages
        song = get_object_or_404(Song, slug=self.kwargs['slug'])
        #  gets url to redirect to
        redirect_url = request.POST.get('redirect_url')

        # storing the tracklist in a http session so that the contents of the tracklist is not overwritten or lost while browsing the site until the browser is closed
        # get the var if it exists or assign it an empty list
        tracklist = request.session.get('tracklist', [])

        # the song's slug is used as its key in the tracklist list
        song_slug = song.slug

        # additional check if its already in their tracklist it displays message and doesnt add to tracklist
        if song_slug in tracklist:
            # messages.error(request, f"You already have {song.name} in your tracklist")
            print(f"You already have {song.name} in your tracklist")
        else:
            # add the song_slug to the tracklist list
            tracklist.append(song_slug)
            print(f'{song.name} added to tracklist')
            # messages.success(request, f"{song.name} has been added to your tracklist")

        # updating the tracklist var in the session dict
        request.session['tracklist'] = tracklist

        # to check the session thing works
        print(request.session['tracklist'])

        # calls the hidden redirect_url input
        return redirect(redirect_url)


class RemoveFromTracklist(View):
    """
    Class based view inheriting Django's View
    Contains the post method for 
    """
    def post(self, request, *args, **kwargs):
        """
        View to remove a song from the tracklist and redirect to the
        same tracklist page
        """

        # getting the song by its pk inorder to include its name in messages
        song = get_object_or_404(Song, slug=self.kwargs['slug'])
        #  gets url to redirect to
        redirect_url = request.POST.get('redirect_url')
        # the song's slug is used as its key in the tracklist list
        song_slug = song.slug

        # get tracklist list from the session
        tracklist = request.session.get('tracklist')

        # checking if the song is in the list and removing it
        if song_slug in tracklist:
            tracklist.remove(song_slug)
            # messages.success(request, f"{song.name} was removed from your tracklist")
            print(f"removed {song.name} from tracklist")
        else:
            print(f'There was an error while trying to remove {song.name} from the tracklist')
            # messages.error(request, f"There was an error while trying to remove {song.name} from your tracklist")

        # updating the tracklist var in the session list
        request.session['tracklist'] = tracklist

        # to check the session thing works
        print(request.session['tracklist'])

        # calls the hidden redirect_url input
        return redirect(redirect_url)

# def remove_from_bag(request, item_id):
#     """
#     View to remove an item from the bag if the remove button is clicked
#     Dont need to get the quantity sincec they will want it to be 0
#     Using a Try Except block to catch any errors since this is posted to via JS
#     Always redirects to the shopping bag
#     """

#     product = get_object_or_404(Product, pk=item_id)

#     try:
#         # get the session if it exists or assign empty dict
#         bag = request.session.get('bag', {})

#         # removing the item from the bag dict
#         bag.pop(item_id)
#         messages.success(request, f"{product.name} has been removed from your bag")

#         # updating the bag var in the session dict
#         request.session['bag'] = bag

#         # posted to via a JS function therefore need to use HttpResponse
#         return HttpResponse(status=200)
#     except Exception as e:
#         # print(e)
#         messages.error(request, f'There was an error when removing {product.name}. {e}')
#         return HttpResponse(status=500)
