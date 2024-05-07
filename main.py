def welcome():
    print("Welcome to the Song Voting System!")
    print("1. Create a new account")
    print("2. Log in")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    accounts = {}
    if choice == '1':
        create_new_account()
    elif choice == '2':
        # Call the login function here
        login(accounts)
        if accounts == {}:
            print("No accounts found. Please create a new account.")
            create_new_account()
    elif choice == '3':
        # Call the exit function here
        exit_program()
    else:
        print("Invalid choice. Please try again.")


def exit_program():
    print("Thank you for using the Song Voting System. Goodbye!")
    exit()

def create_new_account():
    """
    Function to create a new account by taking user input for username and password.
    """
    # Initialize an empty dictionary to store account information
    accounts = {}

    # Prompt user to enter a username
    username = input("Enter a username: ")

    # Check if the username already exists
    while username in accounts:
        print("Username already exists. Please choose a different username.")
        username = input("Enter a username: ")

    # Prompt user to enter a password
    password = input("Enter a password: ")

    # Store the username and password in the dictionary
    accounts[username] = password

    print("Account created successfully!")
    print(f"Username: {username}")
    print(f"Password: {'*' * len(password)}")  # Mask the password

    return accounts

def login(accounts):
    """
    Function to log in to an existing account by verifying the username and password.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists and the password is correct
    if username in accounts and accounts[username] == password:
        print("Login successful!")
        # Call the main function here
        main()
    else:
        print("Invalid username or password. Please try again.")
        # Call the login function again
        login(accounts)

def play_song(song_name):
    """
    Function to simulate playing a song.
    """
    print(f"Now playing: {song_name}")
    input("Press Enter to stop the song...")

def vote_for_song(song_name, votes):
    """
    Function to vote for a song.
    """
    print(f"How do you feel about '{song_name}'?")
    print("1. Like")
    print("2. Dislike")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        feeling = 'like'
    elif choice == '2':
        feeling = 'dislike'
    else:
        print("Invalid choice. Please try again.")
        vote_for_song(song_name, votes)

    comment = input("Enter a comment (optional): ")
    votes[song_name].append((feeling, comment))
    print("Thank you for your vote!")

def main():
    # Initialize an empty dictionary to store song votes
    song_votes = {
        "Song 1": [],
        "Song 2": [],
        "Song 3": [],
        # Add more songs as needed
    }

    while True:
        print("\nWelcome to the Song Voting System!")
        print("1. Play Song 1")
        print("2. Play Song 2")
        print("3. Play Song 3")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            play_song("Song 1")
            vote_for_song("Song 1", song_votes)
        elif choice == '2':
            play_song("Song 2")
            vote_for_song("Song 2", song_votes)
        elif choice == '3':
            play_song("Song 3")
            vote_for_song("Song")
            
            #Looks good

if __name__ == "__main__":
    welcome()
    main()
