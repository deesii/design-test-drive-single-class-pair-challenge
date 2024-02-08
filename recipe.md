# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

- track item {"artist": "", "song": ""}
- track list [track_1, track_2, etc.]

### nouns
- tracks
- list of tracks

### verbs
- add tracks
- see list of tracks

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
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
        pass

    def display_tracks(self):
        # Returns:
        #   A list of dictionaries representing tracks (artist and song)
        # Side-effects:
        #   None
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Initialises TrackTracker instance with an empty list for .track_list
"""
tracker = TrackTracker() #=> tracker.track_list == []

"""
Test add_track and display_tracks methods by adding a new track with a song and artists as strings in a dictionary
"""
tracker = TrackTracker()
tracker.add_track("WHAM!", "Last Christmas") 
tracker.display_tracks() #=> [{"artist": "WHAM!", "song": "Last Christmas"}]

"""
Test add_track and display_tracks methods by adding multiple tracks
"""
tracker = TrackTracker()
tracker.add_track("WHAM!", "Last Christmas")
tracker.add_track("Mitski", "My Love Mine All Mine")
tracker.display_tracks() #=> [{"artist": "WHAM!", "song": "Last Christmas"}, {"artist": "Mitski", "song": "My Love Mine All Mine"}]


"""
As above but testing for empty strings 
"""
tracker = TrackTracker()
tracker.add_track("", "Last Christmas") # => raises esception "Artist and Song arguments must be a non-empty string"

"""
As above but testing for int as argument
"""
tracker = TrackTracker()
tracker.add_track(1, "Last Christmas") # => raises esception "Artist and Song arguments must be a non-empty string"

"""
Test successfully added tracks in list even after an exception is raises later
"""
tracker = TrackTracker()
tracker.add_track("WHAM!", "Last Christmas")
tracker.add_track(1, "Last Christmas") # => raises esception "Artist and Song arguments must be a non-empty string"
tracker.display_tracks() #=> [{"artist": "WHAM!", "song": "Last Christmas"}]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
