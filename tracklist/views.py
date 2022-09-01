from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
            messages.error(request, f"You already have {song.name} in your tracklist")
            print(f"You already have {song.name} in your tracklist")
        else:
            # add the song_slug to the tracklist list
            tracklist.append(song_slug)
            print(f'{song.name} added to tracklist')
            messages.success(request, f"{song.name} has been added to your tracklist")

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
            if len(tracklist) == 0:
                messages.success(request, f"{song.name} was removed from your tracklist. \n Your Tracklist is now empty.")
            else:
                messages.success(request, f"{song.name} was removed from your tracklist.")
        else:
            messages.error(request, f"There was an error while trying to remove {song.name} from your tracklist.")

        # updating the tracklist var in the session list
        request.session['tracklist'] = tracklist

        # to check the session thing works
        print(request.session['tracklist'])

        # calls the hidden redirect_url input
        return redirect(redirect_url)
