
class Media:

    def play(self):
        print("Playing media...")

class Playlist(Media):

    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(song, "added successfully")

    def remove_song(self, song):

        if song in self.songs:
            self.songs.remove(song)
            print(song, "removed")
        else:
            print("Song not found")

    def view_songs(self):

        if len(self.songs) == 0:
            print("Playlist empty")

        else:
            print("\nPlaylist Songs:")

            sorted_songs = sorted(
                self.songs,
                key=lambda x: x.lower()
            )

            for song in sorted_songs:
                print(song)

class User:

    def __init__(self, name):

        self.name = name
        self.radio_stations = []
        self.recent_played = []

    def add_station(self, station):

        self.radio_stations.append(station)
        print("Station added")

    def play_song(self, song):

        self.recent_played.append(song)

        if len(self.recent_played) > 5:
            self.recent_played.pop(0)

        print("Now playing:", song)

    def view_recent(self):

        print("\nRecently Played:")

        for song in self.recent_played:
            print(song)

def save_playlist(songs):

    file = open("playlist.txt", "w")

    for song in songs:
        file.write(song + "\n")

    file.close()

    print("Playlist saved")


def load_playlist():

    try:

        file = open("playlist.txt", "r")

        print("\nSaved Playlist:")

        for line in file:
            print(line.strip())

        file.close()

    except:
        print("No saved playlist found")


print("Welcome to Vehicle Infotainment System")

name = input("Enter user name: ")

user = User(name)
playlist = Playlist()

while True:

    print("\n----- MENU -----")

    print("1. Add Song")
    print("2. Remove Song")
    print("3. View Playlist")
    print("4. Play Song")
    print("5. View Recently Played")
    print("6. Add Radio Station")
    print("7. Save Playlist")
    print("8. Load Playlist")
    print("9. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == "1":

            song = input("Enter song name: ")
            playlist.add_song(song)

        elif choice == "2":

            song = input("Enter song name to remove: ")
            playlist.remove_song(song)

        elif choice == "3":

            playlist.view_songs()

        elif choice == "4":

            song = input("Enter song to play: ")
            user.play_song(song)

        elif choice == "5":

            user.view_recent()

        elif choice == "6":

            station = input("Enter radio station: ")
            user.add_station(station)

        elif choice == "7":

            save_playlist(playlist.songs)

        elif choice == "8":

            load_playlist()

        elif choice == "9":

            print("Exiting system...")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)