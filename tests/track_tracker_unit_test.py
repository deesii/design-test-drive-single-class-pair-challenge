import pytest
from lib.track_tracker import *

"""
Initialises TrackTracker instance with an empty list for .track_list
"""

def test_instantiation():
    tracker = TrackTracker() #=> 
    assert tracker.track_list == []

"""
Test add_track and display_tracks methods by adding a new track with a song and artists as strings in a dictionary
"""

def test_add_track_and_display_tracks():
    tracker = TrackTracker()
    tracker.add_track("WHAM!", "Last Christmas") 
    assert tracker.display_tracks() == [{"artist": "WHAM!", "song": "Last Christmas"}]

"""
Test add_track and display_tracks methods by adding multiple tracks
"""

def test_multiple_tracks():
    tracker = TrackTracker()
    tracker.add_track("WHAM!", "Last Christmas")
    tracker.add_track("Mitski", "My Love Mine All Mine")
    assert tracker.display_tracks() == [{"artist": "WHAM!", "song": "Last Christmas"}, {"artist": "Mitski", "song": "My Love Mine All Mine"}]


"""
As above but testing for empty strings 
"""

def test_exception_raised():
    tracker = TrackTracker()
    with pytest.raises(Exception) as e:
        tracker.add_track("", "Last Christmas") # => raises esception "Artist and Song arguments must be a non-empty string"
    err_msg = str(e.value)
    assert err_msg == "Artist and Song arguments must be a non-empty string"

"""
As above but testing for int as argument
"""

def test_exception_raised_for_int():
    tracker = TrackTracker()
    with pytest.raises(Exception) as e:
        tracker.add_track("WHAM!", 1)
    err_msg = str(e.value)
    assert err_msg == "Artist and Song arguments must be a non-empty string"



"""
Test successfully added tracks in list even after an exception is raises later
"""
def test_added_tracks_survive_exception():
    tracker = TrackTracker()
    tracker.add_track("WHAM!", "Last Christmas")
    with pytest.raises(Exception) as e:
        tracker.add_track(1, "Last Christmas") 
    err_msg = str(e.value)
    assert err_msg == "Artist and Song arguments must be a non-empty string"
    assert tracker.display_tracks() == [{"artist": "WHAM!", "song": "Last Christmas"}]