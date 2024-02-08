class TrackTracker:
    # User-facing properties:
    #   artist: string
    #   song: string
    #   track_list: []

    def __init__(self):
        # Parameters:
        #   track_list
        # Side effects:
        #   Sets track_list to empty list
        self.track_list = []

    def add_track(self, artist, song):
        # Parameters:
        #   artist: string representing artist's name
        #   song: string representing song title
        # Returns:
        #   Nothing
        # Side-effects
        #   create dictionary representing track and appends to track_list
        if  type(artist) != str or type(song) != str or artist == "" or song == "":
            raise Exception("Artist and Song arguments must be a non-empty string")
        track = {"artist": artist, "song": song}
        self.track_list.append(track)

    def display_tracks(self):
        # Returns:
        #   A list of dictionaries representing tracks (artist and song)
        # Side-effects:
        #   None
        return self.track_list