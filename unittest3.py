import pytest
from workingCopy import Song, import_songs_from_csv, recommend_similar_songs

# Test Song class
def test_Song_class():
    song = Song("Title", "Artist", "Genre", 2024, 0.8, 0.7, 90)
    assert song.title == "Title"
    assert song.artist == "Artist"
    assert song.top_genre == "Genre"
    assert song.year == 2024
    assert song.energy == 0.8
    assert song.danceability == 0.7
    assert song.popularity == 90

# Test import_songs_from_csv function
def test_import_songs_from_csv():
    songs = import_songs_from_csv('Top100MostStreamed.csv')
    assert len(songs) == 100
    assert isinstance(songs[0], Song)

# Test recommend_similar_songs function
def test_recommend_similar_songs():
    songs = [
        Song("Song1", "Artist1", "Genre1", 2024, 0.8, 0.7, 90),
        Song("Song2", "Artist2", "Genre2", 2024, 0.6, 0.5, 80),
        Song("Song3", "Artist3", "Genre3", 2024, 0.9, 0.8, 95)
    ]
    liked_song = songs[2]
    recommended_songs = recommend_similar_songs(liked_song, songs)
    assert liked_song not in recommended_songs
