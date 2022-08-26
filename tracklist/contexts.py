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
    """

    # setting up vars
    # list containing song object
    tracklist_songs = []
    tracklist_total = 0
    # get the var if it exists or assign empty list
    tracklist = request.session.get('tracklist', [])

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
        # ELSE ? some note to be triggered in the tracklist that one of their songs was deleted or not found

    context = {
        'tracklist_songs': tracklist_songs,
        'tracklist_total': tracklist_total,
        # 'grand_total': grand_total,  # only need if you use discounts later
    }

    return context
