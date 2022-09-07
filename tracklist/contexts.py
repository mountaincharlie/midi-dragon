"""
contexts file for handling the data that needs to be passed from a number
of templates to the user's My Tracklist page.
Made available across the whole site by adding to settings.py
context_processors
"""
from songs.models import Song


def tracklist_contents(request):
    """
    Context processor
    Returns context dictionary of data for the tracklist
    The function is avaliable accross all the templates

    If updating_tracklist = 'true' the toast_success html snippet
    will display the tracklist overview in the message, else it will
    only show the message text (e.g. when logging in/out or creating
    a new song design project)
    Stores in the updating_tracklist variable wether the tracklist
    is being updated in the session
    Resets updating_tracklist in the SESSION so that it will be set to
    'false' by default unless the AddToTracklist() or
    RemoveFromTracklist() views set it to 'true' again
    """
    # list containing song object
    tracklist_songs = []
    tracklist_total = 0
    # get the var if it exists or assign empty list
    tracklist = request.session.get('tracklist', [])

    updating_tracklist = request.session.get('updating_tracklist', 'false')

    request.session['updating_tracklist'] = 'false'

    # song_slug is the key and the song object is its value
    for song_slug in tracklist:
        # checks that the song exists (not deleted etc)
        if Song.objects.filter(slug=song_slug).exists():
            # get the song
            song = Song.objects.get(slug=song_slug)
            # increasing the tracklist_total
            tracklist_total += song.price
            # add the song to the tracklist_songs list
            tracklist_songs.append(song)

    context = {
        'tracklist_songs': tracklist_songs,
        'tracklist_total': tracklist_total,
        'updating_tracklist': updating_tracklist,
    }

    return context
