import csv
import pandas as pd
import json
import os


class Song:
    def __init__(self, title, artist, top_genre, year, energy, danceability, popularity):
        """
        Initializes a Song object with the attributes provided by the sheet.
        
        Args:
        - title (str): The title of the song.
        - artist (str): The artist of the song.
        - top_genre (str): The genre of the song.
        - year (int): The year the song was released.
        - energy (float): The energy level of the song.
        - danceability (float): The danceability level of the song.
        - popularity (int): The popularity of the song.
        
        Returns:
        - None"""
        self.title = title
        self.artist = artist
        self.top_genre = top_genre
        self.year = year
        self.energy = energy
        self.danceability = danceability
        self.popularity = popularity

    def __repr__(self):
        """
        Returns a string representation of the Song object.
        
        Args:
        - None
        Returns:
        - str: A string representation of the Song object."""
        return f"{self.title} by {self.artist} ({self.year}) - Genre: {self.top_genre}, Energy: {self.energy}, Danceability: {self.danceability}, Popularity: {self.popularity}"


def import_songs_from_csv(filename):
    """
    Opens CSV file and reads in the data to create a list of song objects.
    
    Args:
    - filename (str): The name of the CSV file to import.
    
    Returns:
    - list: A list of Song objects."""
    songs = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = Song(
                row['title'],
                row['artist'],
                row['top genre'],
                int(row['year']),
                float(row['energy']),
                float(row['danceability']),
                int(row['popularity'])
            )
            songs.append(song)
    return songs

class MusicSystem:
    def __init__(self):
        """
        Initializes the MusicSystem class with an empty dictionary and the status of logged in user set as none.
        
        Args:
        - None
        
        Returns:
        - None"""
        self.users = {}
        self.logged_in_user = None

    # Function to create a new account
    def create_account(self):
        """
        Function to create a new account provided a username and password and then stores that in a JSON file.
        
        Args:
        - None
        
        Returns:
        - None"""
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        self.users[username] = password
        with open("users.json", "w") as file:
            json.dump(self.users, file)
        print("Account created successfully.")

    # Function for user login
    def login(self):
        """
        Function to login a provided username and password and checks it against the JSON file.
        
        Args:
        - None
        
        Returns:
        - None"""
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("users.json", "r") as file:
            self.users = json.load(file)
        if username in self.users and self.users[username] == password:
            print("Login successful.")
            self.logged_in_user = username
            main2()
        else:
            print("Invalid username or password.")
            self.welcome_menu()

    def welcome_menu(self):
        """
        Function to display welcome menu to the user.
        
        Args:
        - None
        
        Returns:
        - None"""
        print("Welcome to the Music Recommendation System!")
        print("1. Create an account")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.create_account()
        elif choice == "2":
            self.login()
        elif choice == "3":
            self.exit_program()
        else:
            print("Invalid choice.")

    def exit_program(self):
        """
        Function to exit the program.
        
        Args:
        - None
        
        Returns:
        - None"""
        print("Goodbye!")
        exit()

    def run(self):
        """
        Function to run the program.
        
        Args:
        - None
        
        Returns:
        - None"""
        while True:
            self.welcome_menu()


def main():
    """
    The core login function. It will keep asking the user to login until the user logs in successfully.
    Calls on the function already in the MusicSystem class.
    
    Args:
    - None
    
    Returns:
    - None"""
    while True:
        MusicSystem.welcome_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            MusicSystem.create_account()
        elif choice == "2":
            if MusicSystem.login():
                break
        elif choice == "3":
            MusicSystem.exit_program()
        else:
            print("Invalid choice.")

    print("Now you're logged in. Let's listen to some music!")


# Function to recommend similar songs based on a liked song
def recommend_similar_songs(liked_song, songs, top_n=6):
    """
    Function that performs a similarity calculation between a liked song and a list of songs.
    Calculates Euclidean distance between song attributes and sorts songs by similarity.
    
    Args:
    - liked_song (Song): A Song object representing the liked song.
    - songs (list): A list of Song objects representing all songs.
    - top_n (int): The number of similar songs to recommend.
    
    Returns:
    - list: A list of Song objects representing the top N recommended songs."""
    # Calculate similarity based on song attributes
    similarity_scores = []
    for song in songs:
        # Calculate Euclidean distance between song attributes
        # The lower the distance between two songs, the more similar they are
        similarity_score = sum((getattr(song, attr) - getattr(liked_song, attr)) ** 2 for attr in ['energy', 'danceability', 'popularity'])
        similarity_scores.append((song, similarity_score))
    
    # Sort songs by similarity and get top N similar songs
    # Sorts songs with lower scores first (i.e., more similar songs first)
    sorted_songs = sorted(similarity_scores, key=lambda x: x[1])
    # List comprehesion that splits songs and only considers top N songs
    recommended_songs = [song for song, _ in sorted_songs[1:top_n]]
    
    return recommended_songs

# Function to get user vote on a song
def vote_on_song():
    """
    Function to get user vote on a song.
    
    Args:
    - None
    
    Returns:
    - bool: True if the user liked the song, False if the user did not like the song, None if the vote is invalid."""
    vote = input("Did you like the song? (yes/no): ").strip().lower()
    if vote == 'yes':
        return True
    elif vote == 'no':
        return False
    else:
        print("Invalid vote. Please enter 'yes' or 'no'.")
        return None

def main2():
    """
    Main function to run the music recommendation system.
    Calls on the functions to import songs from a CSV file, get user vote on a song, and recommend similar songs.
    
    Args:
    - None
    
    Returns:
    - None"""
        # Import songs from CSV file
    songs = import_songs_from_csv('Top100MostStreamed.csv')
    for song in songs:
        # User listens to a song
        print("Now playing: ", song)

        # Get user vote
        liked = vote_on_song()
        if liked is not None:
            if liked:
                # Recommend similar songs if the user liked the song
                recommended_songs = recommend_similar_songs(song, songs)
                print("\nRecommended similar songs:")
                for recommended_song in recommended_songs:
                    print(recommended_song)
                break
            else:
                print("Moving to the next song...")
        else:
            print("\nInvalid vote. Please try again later.")

if __name__ == "__main__":
    music_system = MusicSystem()
    music_system.run()
    main()
    main2()