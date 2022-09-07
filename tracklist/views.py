""" views.py for the tracklist app """
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views import View
from songs.models import Song


def view_tracklist(request):
    """
    View to return the tracklist page
    -Stops the superuser being able to access the tracklist
    since they shouldnt be able to buy their own songs
    """
    if request.user.is_superuser:
        messages.info(request, "Redirecting Admin to Site Management.")
        return redirect(reverse('all_songs'))

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
        -gets the song by its pk inorder to include its name in
        messages
        -gets url to redirect to
        -stores the tracklist in a http session so that the content
        of the tracklist is not overwritten or lost while browsing
        the site until the browser is closed
        -gets the var if it exists or assign it an empty list
        -the song's slug is used as its key in the tracklist list
        -additional checks if its already in their tracklist it
        displays message and doesnt add to tracklist

        -sets the updating_tracklist var to 'true' in the session
        so that in toast_success.html it creates the message with
        the tracklist view displayed
        """
        song = get_object_or_404(Song, slug=self.kwargs['slug'])
        redirect_url = request.POST.get('redirect_url')

        tracklist = request.session.get('tracklist', [])

        song_slug = song.slug

        if song_slug in tracklist:
            messages.error(
                request,
                f"You already have {song.name} in your tracklist"
            )
        else:
            # add the song_slug to the tracklist list
            tracklist.append(song_slug)
            messages.success(
                request,
                f"{song.name} has been added to your tracklist"
            )

        # updating the tracklist var in the session dict
        request.session['tracklist'] = tracklist
        request.session['updating_tracklist'] = 'true'

        # to check the session thing works
        print(request.session['tracklist'])

        # calls the hidden redirect_url input
        return redirect(redirect_url)


class RemoveFromTracklist(View):
    """
    Class based view inheriting Django's View
    Contains the post method for removing songs
    from the Tracklist
    """
    def post(self, request, *args, **kwargs):
        """
        View to remove a song from the tracklist and redirect to the
        same tracklist page
        -gets the song by its pk inorder to include its name in
        messages
        -gets url to redirect to
        -the song's slug is used as its key in the tracklist list
        -gets tracklist list from the session
        -checks if the song is in the list and removing it

        -updates the tracklist var in the session list
        -sets the updating_tracklist var to 'true' in the session
        so that in toast_success.html it creates the message with
        the tracklist view displayed
        -
        """
        song = get_object_or_404(Song, slug=self.kwargs['slug'])
        redirect_url = request.POST.get('redirect_url')
        song_slug = song.slug

        tracklist = request.session.get('tracklist')

        if song_slug in tracklist:
            tracklist.remove(song_slug)
            if len(tracklist) == 0:
                messages.success(
                    request,
                    f"{song.name} was removed from your tracklist. \n Your Tracklist is now empty."
                )
            else:
                messages.success(
                    request,
                    f"{song.name} was removed from your tracklist."
                )
        else:
            messages.error(
                request,
                f"There was an error while trying to remove {song.name} from your tracklist."
            )

        request.session['tracklist'] = tracklist
        request.session['updating_tracklist'] = 'true'

        # calls the hidden redirect_url input
        return redirect(redirect_url)
