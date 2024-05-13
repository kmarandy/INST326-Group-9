from workingCopy import Song, import_songs_from_csv
import pytest

def test_Song_class():
    song = Song("Title", "Artist", "Genre", 2024, 0.8, 0.7, 90) #initialize a test Song object and checks that it intializes correctly
    assert song.title == "Title"
    assert song.artist == "Artist"
    assert song.top_genre == "Genre"
    assert song.year == 2024
    assert song.energy == 0.8
    assert song.danceability == 0.7
    assert song.popularity == 90
    
def test_import_songs_from_csv():
    songs = import_songs_from_csv('Top100MostStreamed.csv')  #checks that the right amount of songs are being imported from the csv
    assert len(songs) == 100
    
def test_song_string_representation():
    song = Song("Title", "Artist", "Genre", 2024, 0.8, 0.7, 90)
    expected_output = "Title by Artist (2024) - Genre: Genre, Energy: 0.8, Danceability: 0.7, Popularity: 90"
    assert repr(song) == expected_output