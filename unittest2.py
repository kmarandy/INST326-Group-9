import unittest

# Assume recommend_song and get_song_information are defined in a module named my_functions
from my_functions import recommend_song, get_song_information

class TestSongFunctions(unittest.TestCase):

    def test_recommend_song(self):
        user_votes = {"Song 1": ["like", "great song"]}
        all_votes = {"Song 1": [["like", "great song"]], "Song 2": [["like", "good beat"]]}
        recommended_song = recommend_song(user_votes, all_votes)
        self.assertIn(recommended_song, all_votes.keys())

    def test_get_song_information(self):
        song_name = "Song 1"
        song_database = {"Song 1": {"artist": "Artist 1", "album": "Album 1", "release_date": "2022-01-01"}}
        song_info = get_song_information(song_name, song_database)
        self.assertEqual(song_info["artist"], "Artist 1")
        self.assertEqual(song_info["album"], "Album 1")
        self.assertEqual(song_info["release_date"], "2022-01-01")

if __name__ == '__main__':
    unittest.main()
